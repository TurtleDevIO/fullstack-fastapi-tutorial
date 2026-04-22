# FastAPI Backend

A modern FastAPI backend application built with Python 3.14+.

## Prerequisites

- **UV**: Fast Python package installer and resolver ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))

UV will automatically install the required Python version (3.14+) when you run the project.

## Installation

1. Clone the repository and navigate to the backend directory:
   ```sh
   cd backend
   ```

2. Install dependencies using UV:
   ```sh
   uv sync
   ```

## Development

Start the development server with hot reload:

```sh
uv run fastapi dev main.py
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, you can access:
- **Interactive API docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/redoc

## Code Quality

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

Run the linter:
```sh
uv run ruff check .
```

Format code:
```sh
uv run ruff format .
```

## Project Structure

```
backend/
├── main.py           # Application entry point
├── pyproject.toml    # Project dependencies and configuration
└── README.md         # This file
```
