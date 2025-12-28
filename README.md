# python-modern-tools

> **Note:** This project is a work in progress. Not all tools have been added yet, and the list will continue to grow as the project evolves.

A curated collection of modern tools and utilities for Data Science/AI developer using Python. This project aims to simplify packaging, testing, and development workflows with a focus on best practices and developer productivity.

## Setup for developers

### Sync and install project with `uv`

```bash
just install
```

### `just` commands

```bash
just lint <file-path> # lint, format & type check

just tests # run pytest tests
```

### `pre-commit` commands

```bash
# Run hooks on all files
pre-commit run --all-files

# Run hooks only on staged files
pre-commit run

# Run a specific hook
pre-commit run ruff --all-files

# Commit without running hooks (use sparingly)
git commit -m "WIP" --no-verify
```

## AI & ML

Libraries for AI/ML applications

| Tool | Description | Tool | Description |
|------|-------------|------|-------------|
| **GLiNER** | Zero-shot NER model | **DeepSeek** | Openm-source LLM |
| **Diffbot** | Web scraping API | **Docling** | Document parsing library |
| **FastMCP** | MCP server framework | **LangChain** | LLM application framework |
| **LangGraph** | Agent orchestration | **LlamaIndex** | LLM data framework |
| **MLflow** | ML experiment tracking | **Ollama** | Local LLM runtime |
| **PydanticAI** | AI agent framework | **Sentence Transformers** | Text embeddings |
| **SmolVLM** | Vision language model | **spaCy** | NLP processing pipeline |
| **Transformers** | Hugging Face models |  |

## Data Processing

Libraries for data manipulation and distributed computing

| Tool | Description | Tool | Description |
|------|-------------|------|-------------|
| **CloudQuery** | Cloud ETL platform | **Coiled** | Cloud scaling for Python |
| **delta-rs** | Delta Lake in Rust | **DuckDB** | In-process SQL database |
| **ffn** | Financial analysis library | **polars** | Fast DataFrame library |
| **PySpark** | Distributed processing |  |

## Databases & Search

Database clients, ORMs, and vector search

| Tool | Description | Tool | Description |
|------|-------------|------|-------------|
| **Annoy** | Approximate nearest neighbors | **ChromaDB** | Embedding database |
| **Milvus** | Vector database | **pgvector** | Postgres vector search |
| **Pinecone** | Vector datavase service | **SQLModel** | SQL databse library |

## Developer Tools

Testing, configuration, and development utilities

| Tool | Description | Tool | Description |
|------|-------------|------|-------------|
| **behave** | BDD testing framework | **Cookiecutter** | Project templating |
| **DVC** | Data version control | **Faker** | Fake data generator |
| **Git** | Version control | **Git Submodules** | Nested repositories |
| **Gradio** | ML model interfaces | **Hydra** | Configuration management |
| **Loguru** | Python logging library | **marimo** | Reactive notebooks |
| **mypy** | Static type checker | **Pandera** | DataFrame validation |
| **pdoc** | API documentation | **Poetry** | Dependency management |
| **pre-commit** | Git hook framework | **prek** | Rust-powered pre-commit |
| **Pydantic** | Data validation library | **pytest** | Python testing framework |
| **Ruff** | Python linter and formatter | **ty** | Rust-based type checker |
| **uv** | Python package manager |  |

## Python Built-ins

Standard library modules and features

| Tool | Description | Tool | Description |
|------|-------------|------|-------------|
| **dataclass** | Data class decorator | **difflib** | Sequence matching library |
| **itertools** | Python iteration utilities | **namedtuple** | Immutable data containers |
| **regex** | Pattern matching module | **tempfile** | Temporary file handling |

## Text Processing

String matching and text parsing utilities

| Tool | Description | Tool | Description |
|------|-------------|------|-------------|
| **MarkItDown** | Convert files to Markdown | **PRegEx** | Programmatic regex |
| **pyparsing** | Text parsing library | **RapidFuzz** | Fuzzy string matching |

## Utilities

Specialized tools for specific tasks

| Tool | Description | Tool | Description |
|------|-------------|------|-------------|
| **Codon** | Python JIT compiler | **handcalcs** | Engineering calculations in LaTex |
| **latexify** | LaTex expression generator | **rembg** | Image background removal |
| **SymPy** | Symbolic mathematics | **whenever** | Python datetime library |

## Visualization

Animation and visual content generation

| Tool | Description | Tool | Description |
|------|-------------|------|-------------|
| **adjustText** | Matplotlib label positioning | **Altair** | Declarative visualization |
| **Great Tables** | Publication-ready tables | **Manim** | Math animation engine |
| **Yellowbrick** | ML visualization library |  |
