# Mem0 Project Context

## Project Overview

**Mem0** (pronounced "mem-zero") is a memory layer for AI agents, enabling them to remember user preferences, adapt to individual needs, and continuously learn over time. It provides a unified interface for managing long-term memory across sessions, users, and agents.

*   **Core Logic:** Python-based (`mem0/` directory).
*   **SDKs:** Python (`mem0ai`) and TypeScript (`mem0-ts`).
*   **Infrastructure:** Supports vector databases (Qdrant, Chroma, Pinecone, etc.) and graph databases (Neo4j).
*   **Deployment:** Can be used as a library or a self-hosted server (Docker).

## Directory Structure

*   `mem0/`: Core Python library source code.
*   `mem0-ts/`: TypeScript SDK source code.
*   `server/`: FastAPI-based server implementation for self-hosting.
*   `tests/`: Python unit and integration tests.
*   `docs/`: Documentation (Mintlify).
*   `cookbooks/`: Jupyter notebooks and examples.
*   `examples/`: Various example applications.

## Development Workflow

### Python (Core & Server)

*   **Dependency Management:** Uses `hatch`.
    *   `pyproject.toml` defines dependencies and build configuration.
*   **Environment Setup:**
    *   `hatch env create` to create the environment.
    *   `hatch shell dev_py_3_XX` (e.g., `dev_py_3_11`) to activate a specific Python version environment.
*   **Building:**
    *   `hatch build`: Builds the package.
*   **Testing:**
    *   `make test`: Runs all tests.
    *   `make test-py-3.XX`: Runs tests for a specific Python version.
    *   Under the hood, uses `pytest`.
*   **Linting & Formatting:**
    *   `make format`: Runs `ruff format`.
    *   `make lint`: Runs `ruff check`.
    *   `make sort`: Runs `isort`.

### TypeScript (SDK)

*   **Directory:** `mem0-ts/`
*   **Dependency Management:** Uses `pnpm`.
*   **Building:**
    *   `pnpm build`: Builds the project using `tsup`.
*   **Testing:**
    *   `pnpm test`: Runs tests using `jest`.
*   **Formatting:**
    *   `pnpm format`: Runs `prettier`.

### Server (Docker)

*   **Directory:** `server/`
*   **Running Locally:**
    *   `docker-compose -f server/docker-compose.yaml up`
    *   Starts the Mem0 API server, Postgres (pgvector), and Neo4j.
*   **Configuration:**
    *   Environment variables are loaded from `.env` in the `server/` directory.

## Key Conventions

*   **Code Style:**
    *   Python: Follows `ruff` and `black` profile conventions.
    *   TypeScript: Follows `prettier` standards.
*   **Testing:**
    *   New features must include tests.
    *   All tests must pass across supported Python versions before PR submission.
*   **Versioning:** Follows Semantic Versioning.

## Common Commands

| Task | Command | Context |
| :--- | :--- | :--- |
| **Install Python Env** | `hatch env create` | Root |
| **Run Python Tests** | `make test` | Root |
| **Format Python Code** | `make format` | Root |
| **Lint Python Code** | `make lint` | Root |
| **Install JS Deps** | `pnpm install` | `mem0-ts/` |
| **Build JS SDK** | `pnpm build` | `mem0-ts/` |
| **Run JS Tests** | `pnpm test` | `mem0-ts/` |
| **Start Server** | `docker-compose -f server/docker-compose.yaml up` | Root |
