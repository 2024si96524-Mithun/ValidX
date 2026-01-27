# Contributing to ValidX

Thank you for considering contributing to ValidX! Contributions of all
kinds are welcome --- including code, documentation, bug reports,
feature suggestions, and feedback.

By participating in this project, you agree to follow our Code of
Conduct.

------------------------------------------------------------------------

## Getting Started

### Prerequisites

-   Python 3.9 or higher
-   Git
-   Virtual environment tool (`venv` recommended)

### Setup Instructions

1.  Fork the repository on GitHub\

2.  Clone your fork locally:

    ``` bash
    git clone https://github.com/<your-username>/ValidX.git
    cd ValidX
    ```

3.  Create and activate a virtual environment:

    ``` bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

4.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

------------------------------------------------------------------------

## Branching Strategy

-   `main` → Stable production-ready branch\
-   Create feature branches using meaningful names:
    -   `feature/add-schema-validation`
    -   `bugfix/fix-null-pointer`
    -   `docs/update-readme`

Avoid committing directly to `main`.

------------------------------------------------------------------------

## Making Changes

Please follow these standards before submitting your work:

-   Follow **PEP 8** coding conventions\

-   Use **type hints** wherever possible\

-   Format code using:

    ``` bash
    black .
    isort .
    flake8 .
    ```

-   Run tests:

    ``` bash
    pytest
    ```

------------------------------------------------------------------------

## Commit Message Guidelines

Write clear, meaningful commit messages. Examples:

-   `feat: add new JSON schema validator`
-   `fix: handle empty request payload`
-   `docs: update installation steps`
-   `refactor: simplify validation logic`

------------------------------------------------------------------------

## Submitting a Pull Request

Before submitting your PR, ensure:

-   [ ] Code runs without errors\
-   [ ] Tests are added or updated\
-   [ ] All tests pass successfully\
-   [ ] Code formatted using black/isort\
-   [ ] PR description clearly explains:
    -   What changed
    -   Why it changed
    -   Any impact on existing functionality

A good PR makes reviewing easy.

------------------------------------------------------------------------

## Reporting Issues

If you find a bug or want to suggest a feature, open an issue and
include:

-   Clear title and description\
-   Steps to reproduce (for bugs)\
-   Expected behavior\
-   Actual behavior\
-   Screenshots/logs if applicable\
-   Environment details (Python version, OS)

Well-written issues get resolved faster.

------------------------------------------------------------------------

## Security Issues

If you discover a security vulnerability, **do not create a public
issue**.

Instead, responsibly disclose it to the project maintainers privately.

------------------------------------------------------------------------

## Community Standards

Please be respectful and constructive in all interactions.\
This project follows the Code of Conduct: see `CODE_OF_CONDUCT.md`.

We are building a welcoming and inclusive community.
