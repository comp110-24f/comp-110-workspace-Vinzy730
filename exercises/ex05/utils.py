"""Some utility functions"""

__author__ = "730764770"


def only_evens(random_list: list[int]) -> list[int]:
    # Creates a new list containing only even number
    even_list: list[int] = []
    for elem in random_list:
        if elem % 2 == 0:
            even_list.append(elem)
    return even_list


def sub(random_list: list[int], num1: int, num2: int) -> list[int]:
    # Generate a list which is a subset of the input list, between the specified start
    # index and the end index - 1
    if num1 < 0:
        num1 = 0
    if num2 > len(random_list):
        num2 = len(random_list)
    if len(random_list) == 0 or num1 >= len(random_list) or num2 <= 0:
        return []
    random_num1: list[int] = []
    for idx in range(num1, num2):
        random_num1.append(random_list[idx])
    return random_num1


def add_at_index(random_list: list[int], num: int, index: int) -> None:
    # Modify the input list to place the element at the given index
    idx1: int = index + 1
    idx2: int = index
    random_num1: list[int] = []
    if index < 0 or index > len(random_list):
        raise IndexError("Index is out of bounds for the input list")
    elif len(random_list) == 0 and index == 0:
        random_list.append(num)
    else:
        random_list.append(random_list[len(random_list) - 1])
        for x in random_list:
            random_num1.append(x)
        # had trouble implementing another for loop
        while idx1 < len(random_list):
            random_list[idx1] = random_num1[idx2]
            idx1 += 1
            idx2 += 1
        random_list[index] = num
