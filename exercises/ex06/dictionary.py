"""Dictionary excercise"""

__author__ = "730764770"


def invert(input: dict[str, str]) -> dict[str, str]:
    output: dict[str, str] = {}
    for elem in input:
        # doing the program
        output[input[elem]] = elem
    # key error check
    if len(input) != len(output):
        raise KeyError("Two values are the same so duplicate keys")
    # no need for an empty list check because it is implemented
    return output


def favorite_color(input: dict[str, str]) -> str:
    count: dict[str, int] = {}
    greatest: int = 0
    # empty dictionary check
    if input == {}:
        return ""
    for key in input:
        if input[key] in count:
            count[input[key]] += 1
        else:
            count[input[key]] = 1
    # adding the color and number of times it appears
    for color2 in count:
        if count[color2] >= greatest:
            greatest = count[color2]
        # checking what is the greatest number of appearence
    for color3 in count:
        if count[color3] == greatest:
            return color3
        # returning the color with greatest appearences
    return "How did you get here?"
    # genuine concern, only hear because vscode checker said needed a return here


def count(input: list[str]) -> dict[str, int]:
    count: dict[str, int] = {}
    for word in input:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    output: dict[str, list[str]] = {}
    for word in input:
        if word[0].lower() in output:
            output[word[0].lower()] += [word]
        else:
            output[word[0].lower()] = [word]
    return output


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    if day in attendance:
        idx: int = 0
        day_list: list[str] = attendance[day]
        while idx < len(day_list):
            if student == day_list[idx]:
                return
        attendance[day] += [student]
    else:
        attendance[day] = [student]
