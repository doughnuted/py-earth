# Roadmap: PyEarth Python Rewrite

This document outlines the development roadmap for the new Python-based implementation of PyEarth.

## Phase 1: Core Functionality & Setup (Current)

*   [x] Set up `python-rewrite` branch from original fork point.
*   [x] Create `pyearth_python` directory for the new library.
*   [x] Initialize `roadmap.md`, `agents.md`, `gemini.md`, `jules.md`.
*   [ ] Define core class structure based on original PyEarth (names, methods - Python implementation).
*   [ ] Basic build and packaging setup for `pyearth_python` (e.g., `pyproject.toml`, `setup.cfg`).
*   [ ] Initial test suite structure.

## Phase 2: Reimplementing Core MARS Algorithm

*   [ ] Implement the forward pass of the MARS algorithm.
*   [ ] Implement the backward pass (pruning) of the MARS algorithm.
*   [ ] Basic model fitting (`fit` method).
*   [ ] Basic prediction (`predict` method).
*   [ ] Comprehensive unit tests for core algorithm components.

## Phase 3: Scikit-learn Compatibility

*   [ ] Ensure full compliance with scikit-learn estimator API:
    *   `get_params`, `set_params`
    *   `fit(X, y)`
    *   `predict(X)`
    *   `score(X, y)` (if applicable)
    *   Other relevant mixins and conventions (e.g., input validation).
*   [ ] Add examples of usage with scikit-learn pipelines and model selection tools.
*   [ ] Integration tests with scikit-learn utilities.

## Phase 4: Addressing Original PyEarth Issues & Enhancements

*   [x] Research and list known issues/limitations of the C-based `py-earth` (Completed - see notes below).
*   [ ] Implement solutions or improvements for these issues in the Python version.
    *   **Note on `py-earth` issues:** A review of the original library's GitHub issues reveals that the vast majority relate to difficulties with C compilation, Cython, build dependencies, and binary incompatibilities with specific Python/OS/NumPy versions. **The pure Python nature of this rewrite will inherently resolve these installation and build-related problems.**
    *   Other issues are feature requests (e.g., SymPy export, easier basis function extraction) or potential bugs/performance quirks.
    *   **Strategy for Python Rewrite:**
        *   Installation/build issues: Addressed by design.
        *   Feature requests (like SymPy export #223, enhanced basis function usability #209): Consider for later phases. Ensure basis function objects are well-designed and accessible.
        *   Performance (e.g., #206): Prioritize correctness, then optimize using NumPy. Implement "Fast MARS" parameters.
        *   Parameter defaults (e.g., #205 `zero_tol`): Maintain original defaults for API compatibility initially.
        *   Robustness (e.g., #215 `TypeError`): Ensure strong input validation and comprehensive testing.
*   [ ] Consider potential enhancements (e.g., improved verbosity, SymPy export).

## Phase 5: Advanced Features & Polish

*   [ ] Implement interaction terms.
*   [ ] Handle categorical features.
*   [ ] Allow for different basis functions (if desired beyond standard hinge functions).
*   [ ] Comprehensive documentation (API reference, user guide, examples).
*   [ ] Performance optimization (without premature optimization).

## Phase 6: Repository Management & CI/CD

*   [ ] Set up GitHub Actions for automated testing on push/PR.
*   [ ] Implement code coverage reporting.
*   [ ] Set up linters (e.g., Black, Flake8) and formatters.
*   [ ] Consider automated release process.
*   [ ] Plan for potential separation of `pyearth_python` into its own repository and submodule.

## Phase 7: Beta Testing & Release

*   [ ] Solicit feedback from potential users.
*   [ ] Address reported bugs and issues.
*   [ ] Prepare for an initial stable release.

---
*This roadmap is a living document and will be updated as the project progresses.*
