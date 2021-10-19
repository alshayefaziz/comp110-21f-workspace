"""List utility functions part 2."""

__author__ = "730397680"


def only_evens(even: list[int]) -> list[int]:
    """A function that returns only the even values of a list."""
    evens: list[int] = list()
    if len(even) == 0:
        return evens
    i: int = 0
    while i < len(even):
        item: int = even[i]
        if item % 2 == 0:
            evens.append(item)
        i += 1
    return evens


def sub(sup: list[int], start: int, end_minus_one: int) -> list[int]:
    """A function that takes a list and produces a subset of the list which contains all items from start index to end index -1."""
    sublist: list[int] = list()
    if start < 0:
        start = 0
    if end_minus_one > len(sup):
        end_minus_one = len(sup) - 1
    else:
        end_minus_one = end_minus_one - 1
    if len(sup) == 0 or start > len(sup) or end_minus_one <= 0:
        return sublist
    while start <= end_minus_one:
        item: int = sup[start]
        sublist.append(item)
        start += 1
    return sublist


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """A function that takes two lists and generates a new list which contains all of the items from the firs tlist followed by all of the items in the second list."""
    concatenated: list[int] = list()
    i: int = 0
    if len(first_list) > 0:
        while i < len(first_list):
            concatenated.append(first_list[i])
            i += 1
    i: int = 0
    if len(second_list) > 0:
        while i < len(second_list):
            concatenated.append(second_list[i])
            i += 1
    return concatenated