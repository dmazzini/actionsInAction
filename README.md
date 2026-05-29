# actionsInAction

A simple Python calculator app that only adds two numbers.

## Setup

```bash
uv sync
```

## Run

```bash
uv run add-calculator 2 3
```

## Test and lint

```bash
uv run pytest
uv run ruff check .
```

## Docker

```bash
docker build -t add-calculator .
docker run --rm add-calculator 2 3
```
