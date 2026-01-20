"""
ValidX - A flexible and extensible validation library for Python.

This library provides common validation functions, decorators, and utilities
for validating data in Python applications.
"""

__version__ = "0.1.0"
__author__ = "ValidX Contributors"
__license__ = "MIT"

from validx.validators import (
    is_string,
    is_integer,
    is_float,
    is_email,
    is_url,
    is_boolean,
    is_list,
    is_dict,
    is_none,
    is_in_range,
    has_min_length,
    has_max_length,
)
from validx.exceptions import ValidationError
from validx.decorators import validate_args, validate_return
from validx.utils import is_empty, is_not_empty

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__license__",
    # Validators
    "is_string",
    "is_integer",
    "is_float",
    "is_email",
    "is_url",
    "is_boolean",
    "is_list",
    "is_dict",
    "is_none",
    "is_in_range",
    "has_min_length",
    "has_max_length",
    # Exceptions
    "ValidationError",
    # Decorators
    "validate_args",
    "validate_return",
    # Utils
    "is_empty",
    "is_not_empty",
]
