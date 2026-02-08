# python-modern-tools

> [!IMPORTANT]
> ⚠️ **Note:** This project is a work in progress. Not all tools have been added yet, and the list will continue to grow as the project evolves.

A curated collection of modern tools and utilities for Data Scientists/AI developers using Python. This project aims to simplify packaging, testing, and development workflows with a focus on best practices and developer productivity.

## How to use the project as a template

### 1. Create a new project folder

```bash
mkdir -p <project_name>
cd <project_name>
```

### 2. Install [`uv`](https://github.com/astral-sh/uv)

Follow instructions [here](https://docs.astral.sh/uv/getting-started/installation/); install the latest version from `uv` [github releases](https://github.com/astral-sh/uv/releases).

If you have already installed `uv`, insure you're using the latest version:

```bash
uv self update
```

### 3. Create the project

Answer the carefully to the prompted questions:

```
uvx copier copy https://github.com/klaushajdaraj/python-modern-tools.git .
```

> [!IMPORTANT]
> `Copier` generates a `.copier-answers.yml` file. Commit the file and **never** change it manually.

### 4. Push the project into the repo

```bash
git init --initial-branch=main
just install
git add .
git commit -m "feat: first commit"
git remote add origin <remote_repository_URL>
git push --set-upstream origin main
```

### 5. Update an existing project

1. Move inside your project and make sure that there are no local changes (in case you have local changes, commit or stash them).

2. Update your project to the latest Git tag of the template with the following command:

```bash
uvx copier update --defaults
```

3. Resolve any conflicts and commit the changes.

## Setup for developers

### Sync and install project with `uv`

```bash
just install
```

### `just` commands

```bash
# Lint, format & type check
just lint <file-path>

# Run pytest tests
just tests

# Build the project as a distributable package
just build
```

### `pre-commit` commands

Pre-commit hooks run automatically everytime you add your commits: `git commit -m "commit message"`. However, you can still run them manually:

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

### How to run the `FastAPI` example

```bash
uv run uvicorn python_modern_tools.utilities.create_api_example:app --reload 
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
