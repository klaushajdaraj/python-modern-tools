"""
This module is designed for benchmarking various data processing methods.

It compares the performance of Pandas, Polars and DuckDB for a common data aggregation task.

1. Polars

Polars is a Rust-powered DataFrame library designed for speed that brings multi-threaded
execution and query optimization to Python.

Key capabilities include:

- Speeds up operations by using all available CPU cores by default
- Builds a query plan first, then executes only what’s needed
- Streaming mode for processing datasets larger than RAM
- Expressive method chaining with a pandas-like API

2. DuckDB

DuckDB is an embedded SQL database optimized for analytics that brings database-level
query optimization to local files.

Key capabilities include:

- Native SQL syntax with full analytical query support
- Queries CSV, Parquet, and JSON files directly without loading
- Uses disk storage automatically when data exceeds available memory
- Zero-configuration embedded database requiring no server setup

3. Benchmark Summary Table

At the end of the script, a comparison benchmark table summarizes the performance of Pandas,
Polars, and DuckDB across various operations.
"""

# ruff: noqa: D103, ANN201, PLR2004, ANN003, ANN002, ANN202, ANN001

import time

import duckdb
import numpy as np
import pandas as pd
import polars as pl

# ------------------ Create sample data ------------------

np.random.seed(42)
n_rows = 5_000_000

data = {
    "category": np.random.choice(["Electronics", "Clothing", "Food", "Books"], size=n_rows),
    "region": np.random.choice(["North", "South", "East", "West"], size=n_rows),
    "amount": np.random.rand(n_rows) * 1000,
    "quantity": np.random.randint(1, 100, size=n_rows),
}

df_pandas = pd.DataFrame(data)
df_pandas.to_csv("../../data/sales_data.csv", index=False)
print(f"Created sales_data.csv with {n_rows:,} rows")


# Define a decorator for measuring execution time
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"{func.__name__} took {elapsed_time:.2f} seconds")
        return result, elapsed_time

    return wrapper


# ------------------ Data loading performance ------------------


@time_it
def load_with_pandas():
    return pd.read_csv("../../data/sales_data.csv")


@time_it
def load_with_duckdb():
    return duckdb.sql("SELECT * FROM '../../data/sales_data.csv'").df()


@time_it
def load_with_polars():
    return pl.read_csv("../../data/sales_data.csv")


pandas_df, pandas_load_time = load_with_pandas()
duckdb_df, duckdb_load_time = load_with_duckdb()
polars_df, polars_load_time = load_with_polars()

# ------------------ Query optimization ------------------


@time_it
def pandas_query():
    return pd.read_csv("../../data/sales_data.csv").query("amount > 100").groupby("category")["amount"].mean()


@time_it
def polars_query():
    return (
        pl.scan_csv("../../data/sales_data.csv")
        .filter(pl.col("amount") > 100)
        .group_by("category")
        .agg(pl.col("amount").mean().alias("avg_amount"))
        .collect()
    )


@time_it
def duckdb_query():
    return duckdb.sql(
        """
        SELECT category, AVG(amount) as avg_amount
        FROM '../../data/sales_data.csv'
        WHERE amount > 100
        GROUP BY category
        """
    ).df()


pandas_result, pandas_query_time = pandas_query()
duckdb_opt_time, duckdb_query_time = duckdb_query()
polars_opt_time, polars_query_time = polars_query()

# ------------------ GroupBy performance ------------------

df_pd = pd.read_csv("../../data/sales_data.csv")
df_pl = pl.read_csv("../../data/sales_data.csv")


@time_it
def pandas_groupby():
    return df_pd.groupby("category")["amount"].mean()


@time_it
def polars_groupby():
    return df_pl.group_by("category").agg(pl.col("amount").mean())


@time_it
def duckdb_groupby():
    return duckdb.sql("""
        SELECT category, AVG(amount)
        FROM df_pd
        GROUP BY category
    """).df()


pandas_groupby_result, pandas_groupby_time = pandas_groupby()
duckdb_groupby_result, duckdb_groupby_time = duckdb_groupby()
polars_groupby_result, polars_groupby_time = polars_groupby()

# ------------------ Memory efficiency ------------------

df_pd_mem = pd.read_csv("../../data/sales_data.csv")
pandas_mem = df_pd_mem.memory_usage(deep=True).sum() / 1e3
print(f"pandas memory usage: {pandas_mem:,.0f} KB")


result_pl_stream = (
    pl.scan_csv("../../data/sales_data.csv")
    .group_by("category")
    .agg(pl.col("amount").mean())
    .collect(engine="streaming")  # use 'sink_parquet' for even larger-than-RAM datasets
)

polars_mem = result_pl_stream.estimated_size() / 1e3
print(f"Polars result memory: {polars_mem:.2f} KB")


# Configure memory limit and temp directory
duckdb.sql("SET memory_limit = '500MB'")
duckdb.sql("SET temp_directory = '/tmp/duckdb_temp'")

# DuckDB handles larger-than-RAM automatically
result_duckdb_mem = duckdb.sql("""
    SELECT category, AVG(amount) as avg_amount
    FROM '../../data/sales_data.csv'
    GROUP BY category
""").df()

duckdb_mem = result_duckdb_mem.memory_usage(deep=True).sum() / 1e3
print(f"DuckDB result memory: {duckdb_mem:.2f} KB")


print(f"pandas: {pandas_mem:,.0f} KB (full dataset)")
print(f"Polars: {polars_mem:.2f} KB (result only)")
print(f"DuckDB: {duckdb_mem:.2f} KB (result only)")
print(f"\nPolars uses {pandas_mem / polars_mem:,.0f}× less memory than pandas")
print(f"DuckDB uses {pandas_mem / duckdb_mem:,.0f}× less memory than pandas")

# ------------------ Join operations ------------------

orders_pd = pd.DataFrame(
    {
        "order_id": range(1_000_000),
        "customer_id": np.random.randint(1, 100_000, size=1_000_000),
        "amount": np.random.rand(1_000_000) * 500,
    }
)

customers_pd = pd.DataFrame(
    {
        "customer_id": range(100_000),
        "region": np.random.choice(["North", "South", "East", "West"], size=100_000),
    }
)

orders_pl = pl.from_pandas(orders_pd)
customers_pl = pl.from_pandas(customers_pd)


@time_it
def pandas_join():
    return orders_pd.merge(customers_pd, on="customer_id", how="left")


@time_it
def polars_join():
    return orders_pl.join(customers_pl, on="customer_id", how="left")


@time_it
def duckdb_join():
    return duckdb.sql("""
        SELECT o.*, c.region
        FROM orders_pd o
        LEFT JOIN customers_pd c ON o.customer_id = c.customer_id
    """).df()


pandas_join_time, pandas_join_elapsed = pandas_join()
duckdb_join_time, duckdb_join_elapsed = duckdb_join()
polars_join_time, polars_join_elapsed = polars_join()

# ------------------ Benchmark summary table ------------------

# Collect benchmark results and calculate speedup factors
data = {
    "Operation": [
        "Data Loading",
        "Query Optimization",
        "GroupBy Performance",
        "Join Operations",
    ],
    "Pandas (s)": [
        pandas_load_time,
        pandas_query_time,
        pandas_groupby_time,
        pandas_join_elapsed,
    ],
    "Polars (s)": [
        f"{polars_load_time:.2f} ({pandas_load_time / polars_load_time:.1f}×)",
        f"{polars_query_time:.2f} ({pandas_query_time / polars_query_time:.1f}×)",
        f"{polars_groupby_time:.2f} ({pandas_groupby_time / polars_groupby_time:.1f}×)",
        f"{polars_join_elapsed:.2f} ({pandas_join_elapsed / polars_join_elapsed:.1f}×)",
    ],
    "DuckDB (s)": [
        f"{duckdb_load_time:.2f} ({pandas_load_time / duckdb_load_time:.1f}×)",
        f"{duckdb_query_time:.2f} ({pandas_query_time / duckdb_query_time:.1f}×)",
        f"{duckdb_groupby_time:.2f} ({pandas_groupby_time / duckdb_groupby_time:.1f}×)",
        f"{duckdb_join_elapsed:.2f} ({pandas_join_elapsed / duckdb_join_elapsed:.1f}×)",
    ],
}

# Create a summary table
summary_df = pd.DataFrame(data)

# Print the summary table
print("\nBenchmark Performance Summary:\n")
print(summary_df.to_string(index=False))

# ------------------ Combined pipeline example ------------------

# Step 1: DuckDB for initial SQL query
aggregated = duckdb.sql("""
    SELECT category, region,
           SUM(amount) as total_amount,
           COUNT(*) as order_count
    FROM '../../data/sales_data.csv'
    GROUP BY category, region
""").pl()

# Step 2: Polars for additional transformations
enriched = aggregated.with_columns(
    [
        (pl.col("total_amount") / pl.col("order_count")).alias("avg_order_value"),
        pl.col("category").str.to_uppercase().alias("category_upper"),
    ]
).filter(pl.col("order_count") > 100000)

# Step 3: Convert to pandas for visualization or ML
final_df = enriched.to_pandas()
print(final_df.head())

if __name__ == "__main__":
    pass
