# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-29

### 🎉 Initial Release

We're excited to announce the first release of **ValidX** (validify-py) - a flexible and extensible validation library for Python!

### Added

#### Core Type Validators
- `is_string(value)` - Check if value is a string
- `is_integer(value)` - Check if value is an integer (correctly excludes booleans)
- `is_float(value)` - Check if value is a float
- `is_boolean(value)` - Check if value is a boolean
- `is_list(value)` - Check if value is a list
- `is_dict(value)` - Check if value is a dictionary
- `is_none(value)` - Check if value is None

#### Format Validators
- `is_email(value)` - Validate email addresses with robust regex pattern
- `is_url(value)` - Validate URLs (supports HTTP/HTTPS, localhost, IP addresses, and ports)
- `is_phone(value)` - Validate phone numbers (supports international formats with 9-15 digits, optional + prefix, common separators)

#### Range & Length Validators
- `is_in_range(value, min_value, max_value)` - Check if numeric value is within range (inclusive bounds)
- `has_min_length(value, min_length)` - Check minimum length of strings/collections
- `has_max_length(value, max_length)` - Check maximum length of strings/collections

#### Utility Functions
- `is_empty(value)` - Check if value is empty (None, empty string, or empty collection)
- `is_not_empty(value)` - Check if value is not empty

#### Decorators
- `@validate_args(validator)` - Validate function arguments before execution
- `@validate_return(validator)` - Validate function return values after execution

#### Exception Handling
- `ValidationError` - Custom exception with support for message, value, and field attributes

### Features

- ✨ **Full Type Hints** - Complete type annotation support for better IDE experience and static analysis
- 🚀 **Zero Dependencies** - No external runtime dependencies for the core library
- 🐍 **Python Support** - Compatible with Python 3.9, 3.10, 3.11, 3.12, and 3.13
- 📝 **Comprehensive Documentation** - Detailed docstrings with examples for all functions
- 🧪 **Well Tested** - Comprehensive test suite with high code coverage
- ⚡ **Performance Optimized** - Precompiled regex patterns for email and URL validation

### Developer Experience

- Black code formatting configuration
- isort import sorting configuration
- Flake8 linting setup
- MyPy type checking with strict settings
- pytest with coverage reporting
- tox for multi-environment testing

### Documentation

- Complete API reference
- Getting started guide
- Usage examples
- Contributing guidelines
- Code of conduct

---

**Full Changelog**: https://github.com/2024si96524-Mithun/ValidX/commits/v0.1.0
