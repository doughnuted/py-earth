# Project: pyMARS (formerly py-earth) Modernization

This document outlines the roadmap for modernizing the `py-earth` library, rebranding it as `pyMARS`, and aligning it with modern Python and scikit-learn development standards.

## Task Log

- **2025-06-30:** Project roadmap created and initialized in `gemini.md`.
- **2025-06-30:** Fixed `AttributeError: module 'configparser' has no attribute 'SafeConfigParser'` in `versioneer.py` by replacing `SafeConfigParser` with `ConfigParser`.
- **2025-06-30:** Fixed `AttributeError: 'ConfigParser' object has no attribute 'readfp'` in `versioneer.py` by replacing `readfp` with `read_file`. This continues progress on Task 1.3.

## Phase 1: Foundational Modernization & Stability

This phase focuses on getting the codebase into a buildable, testable, and runnable state on a modern Python environment. These are the highest-priority, foundational steps.

| Task ID | Description | Complexity | Time | Priority / Fruit | Status |
|---|---|---|---|---|---|
| 1.1 | **Automated Python 2 to 3 Conversion:** Run `pyupgrade` and `2to3` to automatically fix syntax, imports, and other common Python 2 idioms. | Low | Low | Low-Hanging | **Pending** |
| 1.2 | **Update `setup.py` Dependencies:** Modify `install_requires` and Python version classifiers to reflect modern standards (Python 3.7+). | Low | Low | Low-Hanging | **Pending** |
| 1.3 | **Resolve Cython Build Errors:** Iteratively run `python setup.py build_ext --inplace --cythonize` and fix compilation errors, focusing on the known issues with SciPy's BLAS/LAPACK headers in `_qr.pyx`. | High | Medium | **Critical Blocker** | **Pending** |
| 1.4 | **Establish Test Runner & Fix Failures:** Replace the deprecated `nosetests` with `pytest`. Run the test suite and fix failures resulting from the Python/dependency updates. | Medium | Medium | High | **Pending** |
| 1.5 | **Project Rename (`py-earth` -> `pyMARS`):** Perform a comprehensive search-and-replace of `pyearth`, `py-earth`, and `Earth` (where appropriate) to `pymars`, `py-mars`, and `MARS`. Update file names and directories. | Medium | Medium | Medium | **Pending** |

## Phase 2: Scikit-learn Compatibility

This phase ensures `pyMARS` works as a first-class citizen within the scikit-learn ecosystem.

| Task ID | Description | Complexity | Time | Priority / Fruit | Status |
|---|---|---|---|---|---|
| 2.1 | **API Alignment:** Ensure the main estimator class inherits from `sklearn.base.BaseEstimator` and relevant mixins (`RegressorMixin`, `ClassifierMixin`). | Medium | Medium | High | **Pending** |
| 2.2 | **Implement `get_params` / `set_params`:** Ensure these methods work correctly for scikit-learn's hyperparameter tuning tools (`GridSearchCV`). | Low | Low | High | **Pending** |
| 2.3 | **Integrate Scikit-learn Utilities:** Use `check_X_y`, `check_array`, and other validation functions from `sklearn.utils` to handle input data robustly. | Medium | Medium | Medium | **Pending** |
| 2.4 | **Pass `check_estimator`:** Run and pass the `sklearn.utils.estimator_checks.check_estimator` tests to formally validate compatibility. | High | High | High | **Pending** |

## Phase 3: Modern Development & Automation

This phase introduces modern tooling for testing, documentation, and CI/CD.

| Task ID | Description | Complexity | Time | Priority / Fruit | Status |
|---|---|---|---|---|---|
| 3.1 | **Setup `pytest` Environment:** Create a `pytest.ini` or `pyproject.toml` configuration for the test suite. | Low | Low | High | **Pending** |
| 3.2 | **CI/CD with GitHub Actions:** Create a workflow (`.github/workflows/ci.yml`) that automatically builds, lints, and tests the package on pushes and pull requests across different Python versions. | Medium | Medium | High | **Pending** |
| 3.3 | **Documentation with Sphinx/MkDocs:** Set up a modern documentation site. Generate API documentation from docstrings and write user guides/tutorials. | High | High | Medium | **Pending** |
| 3.4 | **Code Formatting & Linting:** Integrate `black` for code formatting and `ruff` for linting to ensure consistent code style. | Low | Low | Medium | **Pending** |

## Phase 4: Future Features & Enhancements

This phase explores potential new features to enhance the library's capabilities without overlapping with existing tools.

| Feature Idea | Description |
|---|---|
| **Advanced Visualization** | Integration with modern plotting libraries (e.g., Plotly, Altair) to create interactive plots of basis functions, feature importance, and model diagnostics. |
| **Enhanced Interpretability** | Deeper integration with model interpretability libraries like SHAP. While scikit-learn models have some SHAP support, custom visualizations for MARS-specific structures could be highly valuable. |
| **Improved Categorical Feature Handling** | More seamless and efficient handling of categorical features, potentially through integration with `sklearn.preprocessing` or custom encoding strategies optimized for MARS. |
| **Interaction Term Export** | A utility function to export the learned interaction terms as features that can be used in other downstream models (e.g., linear models, GBDTs). |
| **Gemini CLI Action** | A GitHub Action that uses the Gemini CLI to analyze model results, suggest improvements, or automate parts of the development workflow. |
- **2025-06-30:** Attempted to build `_qr.pyx` with SciPy 1.16. Updated `_types.pxd` for NumPy 2.x and cleaned a debug print in `_qr.pyx`.
