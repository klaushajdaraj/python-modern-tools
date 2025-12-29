"""
This module is designed for benchmarking various data processing methods.

Currently, it includes an implementation using DuckDB, a high-performance, in-process SQL
OLAP database management system.
Future extensions may include comparisons with other tools and libraries.

DuckDB key advantages:

- Zero-configuration SQL querying without database server setup
- Seamless integration with pandas and Polars DataFrames
- Efficient memory management for large-scale data processing
- High-performance execution of complex operations including joins and aggregations
- ACID transaction support ensuring data integrity
- Extensible architecture with a comprehensive extension ecosystem
"""

import time

import duckdb
import numpy as np
import pandas as pd

n_rows = 1_000_000

customers = pd.DataFrame(
    {
        "customer_id": range(n_rows),
        "name": [f"Customer_{i}" for i in range(n_rows)],
        "region": np.random.choice(["North", "South", "East", "West"], n_rows),
        "segment": np.random.choice(["A", "B", "C"], n_rows),
    }
)

# customers.to_csv("data/customers.csv", index=False)


# ------------------ Pandas aggregation ------------------

start_time = time.time()
pandas_agg = customers.groupby(["region", "segment"]).size().reset_index(name="count")
pandas_time = time.time() - start_time


# ------------------ DuckDB aggregation ------------------

start_time = time.time()
duckdb_agg = duckdb.sql("""
    SELECT region, segment, COUNT(*) as count FROM customers GROUP BY region, segment
""").df()
duckdb_time = time.time() - start_time

# ------------------ Results ------------------

print(f"Pandas aggregation time: {pandas_time:.2f} seconds")
print(f"DuckDB aggregation time: {duckdb_time:.2f} seconds")
print(f"Speedup: {pandas_time / duckdb_time:.1f}x")
