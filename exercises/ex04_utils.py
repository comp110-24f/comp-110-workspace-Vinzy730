"""Recreating common list methods"""

__author__ = "730764770"


def all(input: list[int], num: int) -> bool:
    idx: int = 0
    if len(input) == 0:
        return False
    while idx < len(input):
        if input[idx] != num:
            return False
        idx += 1
    return True


def max(input: list[int]) -> int:
    idx: int = 0
    big_num: int = input[idx]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        while idx < len(input):
            if big_num < input[idx]:
                big_num = input[idx]
            idx += 1
        return big_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    idx: int = 0
    if len(list_1) != len(list_2):
        return False
    while idx < len(list_1):
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    return True


def extend(og_list: list[int], add_list: list[int]) -> None:
    idx: int = 0
    while idx < len(add_list):
        og_list.append(add_list[idx])
        idx += 1
    if len(og_list) == 0:
        og_list = og_list
