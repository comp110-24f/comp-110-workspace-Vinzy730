"""Practice with while loops with string index"""

__author__ = "730764770"


def num_instances(phrase: str, search_char: str) -> int:
    # Issue: index out of range because index occured before string check -> rearranged
    # Issue: infinite loop because inde+=1 was not in loop because improper indentation
    index: int = 0
    count: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count
