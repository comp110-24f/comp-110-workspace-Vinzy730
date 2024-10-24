"""Tests for utility functions"""

__author__ = "730764770"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_use_case_1() -> None:
    # Testing only_evens returns a list of only all even numbers
    random_list: list[int] = [1, 21, 5, 73, 8]
    assert only_evens(random_list) == [8]


def test_only_evens_use_case_2() -> None:
    # Testing only_evens does not modfiy input list
    random_list: list[int] = [1, 3, 5, 21, 7, 8]
    only_evens(random_list)
    assert random_list == random_list


def test_only_evens_edge_case() -> None:
    # Testing only_evens on empty list
    random_list: list[int] = []
    only_evens(random_list)
    assert random_list == []


def test_sub_use_case_1() -> None:
    # Testing sub generates a list which is a subset of the input list, between the specified start index and the end index
    random_list: list[int] = [1, 2]
    random_num1: int = 0
    random_num2: int = 2
    assert sub(random_list, random_num1, random_num2) == [1, 2]


def test_sub_use_case_2() -> None:
    # Testing sub does not modify input list
    random_list: list[int] = [1, 2]
    random_num1: int = 0
    random_num2: int = 2
    sub(random_list, random_num1, random_num2)
    assert random_list == random_list


def test_sub_edge_case() -> None:
    # Testing sub with start index greater than or equal to length of input list and end index is at most 0 to return an empty list
    random_list: list[int] = [1, 2]
    random_num1: int = 5
    random_num2: int = 0
    assert sub(random_list, random_num1, random_num2) == []


def test_add_at_index_use_case_1() -> None:
    # Testing add_at_index modifies the input list
    random_list: list[int] = [1, 2, 3]
    random_num1: int = 1
    random_num2: int = 2
    add_at_index(random_list, random_num1, random_num2)
    assert random_list == [1, 2, 1, 3]


def test_add_at_index_use_case_2() -> None:
    # Testing add_at_index places element at given index within the input list
    random_list: list[int] = [1, 2, 3, 4, 5]
    random_num1: int = 1
    random_num2: int = 2
    add_at_index(random_list, random_num1, random_num2)
    assert random_list == [1, 2, 1, 3, 4, 5]


def test_add_at_index_edge_case() -> None:
    # Testing add_at_index on empty list
    random_list: list[int] = []
    random_num1: int = 4
    random_num2: int = 0
    add_at_index(random_list, random_num1, random_num2)
    assert random_list == [4]
