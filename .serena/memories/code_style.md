# Code Style and Conventions

## Python
*   **Linting & Formatting**: Enforced via `ruff`. Uses `black` profile for `isort`.
    *   Run `make format` and `make lint` before committing.
*   **Docstrings**: Google-style docstrings (or similar structured format) with `Args:` and `Returns:` sections.
    *   Example:
        ```python
        def add(self, messages: Union[str, List[Dict[str, str]]], ...) -> Dict[str, Any]:
            """
            Create a new memory.

            Args:
                messages (str or List[Dict[str, str]]): Messages to store...
            
            Returns:
                Dict[str, Any]: The created memory.
            """
        ```
*   **Type Hints**: Extensive use of type hints (`typing` module).

## TypeScript
*   **Formatting**: Enforced via `prettier`.
*   **Style**: Standard TypeScript conventions.

## General
*   **Commits**: Use descriptive commit messages.
*   **Tests**: Ensure all tests pass before submitting PRs. Add tests for new features/bug fixes.
