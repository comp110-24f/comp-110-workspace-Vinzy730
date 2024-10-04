"""get_coords function"""

__author__ = "730764770"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    while index1 < len(xs):
        index2: int = 0  # had to set index 2 to 0 to reset the 2nd while loop
        while index2 < len(ys):
            print("(" + xs[index1] + "," + ys[index2] + ")")
            index2 += 1
        index1 += 1
