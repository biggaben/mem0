# Project Overview: Mem0

Mem0 is a memory layer designed to personalize AI interactions by retaining user, session, and agent state. It enables AI agents to remember preferences, adapt to individual needs, and learn over time.

## Key Components
*   **Core Library (`mem0/`)**: Python package `mem0ai`. Manages memory operations (add, search, update, delete) and orchestrates LLMs and Vector Stores.
*   **TypeScript SDK (`mem0-ts/`)**: Node.js/TypeScript client `mem0ai`.
*   **OpenMemory (`openmemory/`)**: Self-hosted platform with a Python backend and React/Next.js frontend.
*   **Server (`server/`)**: Standalone server implementation.

## Tech Stack
*   **Languages**: Python (>=3.9), TypeScript.
*   **Package Management**: `uv` / `hatch` (Python), `pnpm` / `npm` (TypeScript).
*   **Storage**: Vector DBs (Qdrant, Chroma, Pinecone, etc.) and Graph DBs (Neo4j, Memgraph).
*   **LLMs**: Agnostic support (OpenAI, Anthropic, etc.).
*   **Tools**: `ruff`, `isort`, `pytest` (Python); `prettier`, `tsup`, `jest` (TypeScript).

## Structure
*   `mem0/`: Core Python source code.
*   `mem0/memory/main.py`: Main `Memory` class definition.
*   `mem0/vector_stores/`: Vector database implementations.
*   `mem0/llms/`: LLM integrations.
*   `mem0-ts/`: TypeScript SDK source.
*   `openmemory/`: Self-hosted platform source.
*   `server/`: Standalone server source.
*   `tests/`: Python unit and integration tests.
