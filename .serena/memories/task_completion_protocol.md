# Task Completion Protocol

When a task is completed:

1.  **Verify**: Ensure the code works as expected.
2.  **Lint & Format**:
    *   For Python: Run `make format` and `make lint`. Fix any errors.
    *   For TypeScript: Run `npm run format` (in `mem0-ts`).
3.  **Test**:
    *   Run relevant tests using `make test` (Python) or `npm run test` (TypeScript).
    *   If new functionality was added, ensure new tests are included and pass.
4.  **Documentation**: Update docstrings and relevant documentation files if public APIs or behaviors changed.
5.  **Clean up**: Remove any temporary files or debug prints.
