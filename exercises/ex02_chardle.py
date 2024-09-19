"""EX02 - Chardle - A step towards Wordle."""

__author__ = "730764770"


def input_word() -> str:
    # Gets the word for the game
    word_guess: str = input("Enter a 5-character word: ")
    if len(word_guess) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word_guess


def input_letter() -> str:
    # Gets the guessed letter
    letter_guess: str = input("Enter a single character: ")
    if len(letter_guess) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter_guess


def contains_char(word: str, letter: str) -> None:
    # Checks the guessed letter against saved word and outputs the cases
    letter_count: int = 0
    print("Searching for " + letter + " in " + word)
    if letter == word[0]:
        print(letter + " found at index 0")
        letter_count = letter_count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        letter_count = letter_count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        letter_count = letter_count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        letter_count = letter_count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        letter_count = letter_count + 1
    # issue with if statements, overthought the complexity and attempted to use else
    # if instead of multiple if statements
    if letter_count == 0:
        print("No instances of " + letter + " found in " + word)
    elif letter_count == 1:
        print(str(letter_count) + " instance of " + letter + " found in " + word)
    else:
        print(str(letter_count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
