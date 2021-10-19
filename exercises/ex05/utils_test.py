"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "73039680"


def test_only_evens_empty() -> None:
    """Only_evens test 1."""
    even: list[int] = []
    assert only_evens(even) == []


def test_only_evens_only_odds() -> None:
    """Only_evens test 2."""
    even: list[int] = [1, 3, 5]
    assert only_evens(even) == []


def test_only_evens_regular() -> None:
    """Only_evens test 3."""
    even: list[int] = [1, 2, 3, 4, 6, 8, 9]
    assert only_evens(even) == [2, 4, 6, 8]


def test_sub_regular() -> None:
    """Sub test 1."""
    sub_list: list[int] = [3, 6, 9, 0, 2]
    start: int = 3
    end: int = 5
    assert sub(sub_list, start, end) == [0, 2]


def test_sub_empy_list() -> None:
    """Sub test 2."""
    sub_list: list[int] = list()
    start: int = 3
    end: int = 5
    assert sub(sub_list, start, end) == []


def test_sub_negative_start_large_end() -> None:
    """Sub test 3."""
    sub_list: list[int] = [3, 2, 7, 4, 9]
    start: int = -3
    end: int = 32
    assert sub(sub_list, start, end) == [3, 2, 7, 4, 9]


def test_concat_regular() -> None:
    """Concat test 1."""
    first: list[int] = [3, 6, 9]
    second: list[int] = [2, 4, 6]
    assert concat(first, second) == [3, 6, 9, 2, 4, 6]


def test_concat_first_list_empty() -> None:
    """Concat test 2."""
    first: list[int] = list()
    second: list[int] = [2, 4, 6]
    assert concat(first, second) == [2, 4, 6]


def test_concat_second_list_empty() -> None:
    """Concat test 3."""
    first: list[int] = [3, 6, 9]
    second: list[int] = list()
    assert concat(first, second) == [3, 6, 9]