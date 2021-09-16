"""CQ2. Function Calls."""


def a(x: int) -> int:
    """A function."""
    x = x // 2
    if x == 1:
        return 0
    else:
        return 1


def b(x: int) -> int:
    """B function."""
    x = a(x + 1)
    return x


x: int = 2
print