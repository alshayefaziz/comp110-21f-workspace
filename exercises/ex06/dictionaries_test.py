"""Unit tests for dictionary functions."""

import pytest
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730397680"


def test_invert_single() -> None:
    """Invert test 1."""
    vice: dict[str, str] = {"A": "Aziz"}
    assert invert(vice) == {"Aziz": "A"}


def test_invert_ker_error() -> None:
    """Invert test KeyError."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_empty() -> None:
    """Invert test 2."""
    vice: dict[str, str] = {}
    assert invert(vice) == {}


def test_invert_multiple() -> None:
    """Invert Test 3."""
    vice: dict[str, str] = {"A": "Apple", "B": "Banana", "C": "Cantalope"}
    assert invert(vice) == {"Apple": "A", "Banana": "B", "Cantalope": "C"}


def test_favorite_color_regular() -> None:
    """Favorite Color Test 1."""
    vice: dict[str, str] = {"Aziz": "green", "Loaey": "blue", "Yaseen": "blue"}
    assert favorite_color(vice) == "blue"


def test_favorite_color_tie() -> None:
    """Favorite Color Test 2."""
    vice: dict[str, str] = {"Aziz": "green", "Loaey": "blue", "Hamzah": "blue", "Maraam": "red", "Yaseen": "green"}
    assert favorite_color(vice) == "blue"


def test_favorite_color_empty() -> None:
    """Favorite Color Test 3."""
    vice: dict[str, str] = {}
    assert favorite_color(vice) == ""


def test_count_small() -> None:
    """Count Test 1."""
    vice: list[str] = ["a", "b", "c", "a"]
    assert count(vice) == {"a": 2, "b": 1, "c": 1}


def test_count_big() -> None: 
    """Count Test 2."""
    vice: list[str] = ["a", "a", "b", "a", "c", "a", "b", "c", "c", "a", "d", "b"]
    assert count(vice) == {"a": 5, "b": 3, "c": 3, "d": 1}
    

def test_count_empty() -> None:
    """Count Test 3."""
    vice: list[str] = []
    assert count(vice) == {}