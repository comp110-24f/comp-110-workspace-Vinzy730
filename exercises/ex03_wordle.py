"""Wordle copy"""

__author__ = "730764770"


def input_guess(char_idx: int) -> str:
    "compares number of letters in"
    guess: str = input(f"Enter a {str(char_idx)} character word: ")
    while len(guess) != char_idx:
        guess = input(f"That wasn't {str(char_idx)} chars! Try again: ")
    return guess


def contains_char(secret: str, char: str) -> bool:
    """Compares the word and guess character and return True or False"""
    assert len(char) == 1
    idx: int = 0
    count: int = 0
    # difficulty returning the boolean beacuse in the while loop
    while idx < len(secret):
        if secret[idx] == char:
            count += 1
        idx += 1
    if count > 0:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Compare guess and secret words and return a strong of emojis"""
    assert len(guess) == len(secret)
    idx: int = 0
    output: str = ""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    # difficulty arranging the if loops to properly output the emojies
    while idx < len(secret):
        if secret[idx] == guess[idx]:
            idx += 1
            output = output + green_box
        elif contains_char(secret, guess[idx]):
            idx += 1
            output = output + yellow_box
        else:
            idx += 1
            output = output + white_box
    return output


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    moves: int = 1
    guess: str = ""
    while (moves < 7) & (guess != secret):
        print(f"=== Turn {str(moves)}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(secret, guess))
        # forgot emojified returns and not print emojies
        moves += 1
    if guess == secret:
        print(f"You won in {moves}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
