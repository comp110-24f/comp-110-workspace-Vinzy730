"""Imports Concat amd Coords func and some variables and outputs"""

__author__ = "730764770"

from CQs.cq04.concatenation import concat  # type: ignore
from CQs.cq04.coordinates import get_coords

# the from portion in concat is mad and idk why, it works but gives a red underline

x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)
