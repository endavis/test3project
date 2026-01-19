"""Core functionality for test3project."""


def greet(name: str = "World") -> str:
    """Return a greeting message.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting message string.

    Examples:
        >>> greet()
        'Hello, World!'
        >>> greet("Python")
        'Hello, Python!'
    """
    return f"Hello, {name}!"
