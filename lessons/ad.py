"""A funny program."""


def three() -> int:
    x: int = one(3)
    print("three")
    return x + 1


def two() -> int:
    x: int = 2
    print("two")
    return x


def one(x: int) -> int:
    x = x + two()
    print("one")
    return x


print((three))