"""Finds and removes the largest number"""

__author__ = "730764770"


def find_and_remove_max(a: list[int]) -> int:
    if len(a) == 0:
        return -1
    else:
        biggest_num: int = 0
        idx1: int = 0
        "attempted for in loops, didn't work, need to test in free time"
        while idx1 < len(a):
            if biggest_num < a[idx1]:
                biggest_num = a[idx1]
            idx1 += 1
        idx2: int = 0
        "Had trouble with this loop because for loops auto increment, only want to"
        "increment when not removing the max"
        while idx2 < len(a):
            if biggest_num == a[idx2]:
                a.pop(idx2)
            else:
                idx2 += 1
        return biggest_num
