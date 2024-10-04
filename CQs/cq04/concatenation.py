"""concat function"""

__author__ = "730764770"

word1: str = "happy"
word2: str = "tuesday"


def concat(a: str, b: str) -> str:
    c: str = a + b  # didn't think this would work, easy and simple concat
    return c


if __name__ == "__main__":
    print(concat(word1, word2))
# is there any other names we could use?
