default:
    just --list

chmod:
    @chmod +x ./scripts/*.sh

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
    set -ex
    uv run pytest tests -v
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
    @echo "All tests passed!"

print-version: chmod
    @./scripts/print-version.sh

init-docs: chmod
    set -ex
    uv sync
    @./scripts/init-docs.sh

github-pages: chmod
    @./scripts/github-pages.sh

github-tag: chmod
    @./scripts/github-tag.sh

build:
    @echo "Building the project as a distributable package..."
    set -ex
    rm -rvf ./dist
    uv build

docker-build:
    @echo "Building the Docker image..."
    set -ex
    docker build -t python_modern_tools:latest -f scripts/docker/Dockerfile .
