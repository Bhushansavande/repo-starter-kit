"""Replace this package with your own code."""

__version__ = "0.1.0"


def greet(name: str) -> str:
    """Return a greeting. A tiny function so the tests and CI have something real to run."""
    if not name.strip():
        raise ValueError("name must not be empty")
    return f"Hello, {name.strip()}!"
