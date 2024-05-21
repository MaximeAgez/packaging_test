# https://docs.python.org/3/reference/import.html#regular-packages
"""
`test` is a Python package for testing purposes.
"""

# https://docs.python.org/3/tutorial/modules.html#importing-from-a-package
__all__ = (
    "__version__",
    "hello_world",
)

__version__ = "0.0.1"

from .printing import hello_world