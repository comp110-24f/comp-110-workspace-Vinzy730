"""Practice writing unit tests"""

__author__ = "730764770"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_case1() -> None:
    "returns an expected value"
    a: list[int] = [1, 2, 3, 4, 5]
    assert find_and_remove_max(a) == 5


def test_find_and_remove_max_case2() -> None:
    "mutates input"
    a: list[int] = [1, 24, 3, 4, 5]
    assert find_and_remove_max(a)
    assert input == [1, 3, 4, 5]


def test_find_and_remove_max_edge_case() -> None:
    "returns an correct value in case unconventional input"
    a: list[int] = []
    assert find_and_remove_max(a) == -1 and a == []
