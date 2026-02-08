# python-modern-tools

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

## Installation

### 1. Install `uv` as described in `README.md`

### 2. Clone the repo

```bash
git clone https://github.com/klaushajdaraj/python-modern-tools
cd python-modern-tools
```

### 3. Sync the project

```bash
just install
```

Congratulations! You're now ready to use your new project :sparkles:

## Documentation

The project documentation is generated automatically by parsing the source code, provided that the code is properly commented with appropriate docstrings.

To initialize the documentation, run:
```bash
just init-docs
```

To publish the generated documentation to GitHub Pages, run:

```bash
just github-pages
```

After publishing, the documentation will be available at `https://klaushajdaraj.github.io/python-modern-tools/`.

## `justfile` commands

- `just build` — Build the project as a package.
- `just install` — Runs `uv sync` to synch & install the project.
- `just lint` — Formatting and linting with `ruff`.
- `just init-docs` — Runs `scripts/init-docs.sh` to initialize documentation branch.
- `just github-pages` — Runs `scripts/github-pages.sh` to publish documentation to GitHub Pages.
- `just github-tag` — Runs `scripts/github-tag.sh` to create a GitHub tag.
- `just print-version` — Runs `scripts/print-version.sh` to print the current version.
- `just tests` — Runs `scripts/tests.sh` to execute tests.
- `just docker-build` — Runs `scripts/docker-build.sh` to build the Docker image.

## Marimo playground

The Marimo notebook can be run locally using the following command:

```bash
uv run marimo edit
```

This opens the Marimo editor for interactive notebook development.