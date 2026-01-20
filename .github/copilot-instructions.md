# ValidX Project Setup Instructions

## Progress Tracking
- [x] Verify that the copilot-instructions.md file in the .github directory is created.
- [x] Clarify Project Requirements
- [x] Scaffold the Project
- [x] Customize the Project
- [x] Install Required Extensions
- [x] Compile the Project
- [ ] Create and Run Task
- [ ] Launch the Project
- [x] Ensure Documentation is Complete

## Project Information
- **Project Name**: ValidX
- **Type**: Python validation library
- **License**: MIT
- **Purpose**: Open-source validation library for Python with extensible validation rules

## Development Commands
```bash
# Install in development mode
pip install -e .[dev]

# Run tests
pytest

# Run linting
flake8 src tests
black --check src tests
isort --check-only src tests

# Format code
black src tests
isort src tests

# Type checking
mypy src
```
