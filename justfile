default:
    just --list

install:
    @echo "Syncing and installing the project with uv..."
    uv sync

lint PATH:
    @echo "Performing linting on {{PATH}}..."
    uvx ruff check {{PATH}} --fix

    @echo "Performing formatting check on {{PATH}}..."
    uvx ruff format {{PATH}} --check

    @echo "Performing type checking on {{PATH}}..."
    uvx ty check {{PATH}}

tests:
    uv run pytest tests -v
    @echo "All tests passed!"

build:
    @echo "Building the project as a distributable package..."
    uv build