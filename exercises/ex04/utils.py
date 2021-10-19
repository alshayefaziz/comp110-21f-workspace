"""List utility functions."""

__author__ = "730397680"


def all(sample: list[int], given: int) -> bool:
    """A function checking if all the items in a sample match a given numebr."""
    i: int = 0
    if len(sample) == 0:
        return False
    else:
        while i < len(sample):
            item: int = sample[i]
            if item != given:
                return False
            i += 1
    return True


def is_equal(first_set: list[int], second_set: list[int]) -> bool:
    """A function that checks if all the itmes in two sets are equivalent to one another."""
    i: int = 0
    if len(first_set) != len(second_set):
        return False
    else:
        while i < len(first_set) or i < len(second_set):
            first_item: int = first_set[i]
            second_item: int = second_set[i]
            if first_item == second_item:
                i += 1 
            else: 
                return False
    return True


def max(input: list[int]) -> int:
    """A funciton that returns the max value from a set of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    else: 
        i: int = 1
        biggest: int = input[0]
        while i < len(input):
            if input[i] > biggest:
                biggest = input[i]
                i += 1
            else:
                i += 1
    return biggest