# Examples

## Basic Usage
```python
from validx import validators

validators.is_string("hello")  # True
validators.is_email("test@example.com")  # True
```

## Using Decorators
```python
from validx.decorators import validate_args
from validx.exceptions import ValidationError

def is_positive(x):
    return x > 0

@validate_args(is_positive)
def foo(x):
    return x

foo(5)  # Passes
# foo(-1)  # Raises ValidationError
```
