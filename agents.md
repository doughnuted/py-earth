# Agent Instructions for `py-earth` Python Rewrite

This document provides general instructions for AI agents working on this repository.

## General Principles

1.  **Follow the Plan:** Adhere to the current plan outlined by Jules or the lead developer. If the plan needs modification, discuss it first.
2.  **Clarity and Communication:** Clearly state your intentions and the actions you are taking. Use `message_user` for updates or if you require clarification.
3.  **Code Quality:** Write clean, maintainable, and well-documented Python code.
4.  **Testing:**
    *   Write unit tests for new functionality.
    *   Ensure all tests pass before submitting changes.
    *   Aim for high test coverage.
5.  **Commits:**
    *   Make small, logical commits.
    *   Write clear and concise commit messages following conventional formats (e.g., imperative mood, subject line < 50 chars).
    *   Reference relevant issue numbers if applicable.
6.  **Modularity:** The `pyearth_python` directory is intended to become a standalone library. Design it with this in mind, minimizing tight coupling with the parent repository.
7.  **Scikit-learn Compatibility:** A primary goal is full scikit-learn compatibility. All estimators should follow scikit-learn's API and conventions. Refer to the scikit-learn developer documentation.
8.  **Documentation:**
    *   Keep `roadmap.md` updated with progress.
    *   Document public APIs with clear docstrings (e.g., NumPy/SciPy docstring standard).
    *   Add usage examples where appropriate.
9.  **File Management:**
    *   This `agents.md` and other agent-specific files (`jules.md`, `gemini.md`) should be updated as needed and included in commits.
    *   The `pyearth_python` directory will house all the new library code.

## Development Workflow (Planned)

*   **Branching:** Development will happen on the `python-rewrite` branch or feature branches off it.
*   **Pull Requests:** (Once collaboration starts) Changes should be submitted via Pull Requests for review.
*   **CI/CD:** GitHub Actions will be used for automated testing, linting, and potentially releases.
    *   Ensure your changes pass all CI checks.
*   **Linters/Formatters:** We will use Black for code formatting and Flake8 for linting. Please ensure your code conforms.

## Specific Instructions for `pyearth_python`

*   **Language:** Python 3.8+
*   **Core Dependencies (to be determined):** NumPy, SciPy.
*   **Testing Framework:** pytest.
*   **Packaging:** `pyproject.toml` with a modern build backend (e.g., Hatch, Flit, or Poetry).

## Addressing `py-earth` (C version) issues

*   Consult `roadmap.md` and specific issues/discussions for known limitations of the original `py-earth` that need to be addressed in this Python version.

---
*This document is subject to updates. Please check it regularly.*
