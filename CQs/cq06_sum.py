"""Summing the elements of a list using different loops"""

__author__ = "730764770"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for value in vals:
        sum += value
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
