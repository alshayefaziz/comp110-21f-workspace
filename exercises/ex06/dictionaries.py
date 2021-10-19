"""Practice with dictionaries."""

__author__ = "730397680"


def invert(sent: dict[str, str]) -> dict[str, str]:
    """A function in where the sent keys and values are inverted."""
    c: int = 0
    for error in sent:
        for error_test in sent:
            if sent[error] == sent[error_test]:
                c += 1
        if c > 1:
            raise KeyError("Multiple keys are not allowed in dictionaries!")
        else:
            c = 0
    inverted_sent: dict[str, str] = {}
    for new in sent:
        former: str = sent[new]
        latter: str = new
        inverted_sent[former] = latter
    return inverted_sent


def favorite_color(color: dict[str, str]) -> str:
    """A function that takes a set of names and the persons favorite colors and returns the most popular color."""
    counter: int = 0
    counter_2: int = 0
    popular: str = ""
    for colour in color:
        for repeat in color:
            if color[colour] == color[repeat]:
                counter += 1
        if counter > counter_2:
            popular = color[colour]
            counter_2 = counter
            counter = 0
    return popular


def count(input: list[str]) -> dict[str, int]:
    """A function that assigns a list to the key of a dictionary and the value is the amount of times a value appears in an input list."""
    data: dict[str, int] = {}
    for frequency in input:
        if frequency in data:
            data[frequency] += 1
        else:
            data[frequency] = 1
    return data