# Suggested Commands

## Python Development (Root)
The project uses `hatch` for environment management and `make` for convenience.

*   **Setup**: `hatch env create` or `make install`
*   **Format**: `make format` (runs `ruff format`)
*   **Sort Imports**: `make sort` (runs `isort`)
*   **Lint**: `make lint` (runs `ruff check`)
*   **Test**: `make test` (runs `pytest` in default env)
    *   Specific versions: `make test-py-3.9`, `make test-py-3.10`, etc.
*   **Build**: `make build` (runs `hatch build`)

## TypeScript Development (`mem0-ts/`)
*   **Install**: `pnpm install` or `npm install`
*   **Build**: `npm run build`
*   **Test**: `npm run test`
*   **Format**: `npm run format`

## OpenMemory (`openmemory/`)
*   **Build**: `make build`
*   **Run**: `make up`

## Server (`server/`)
*   Check `server/Makefile` if available for specific commands.
