"""Practice  with conditionals, local variables, and user input"""

__author__ = "730764770"


def guess_a_number() -> None:
    """user guesses a secret number predefined and gives feedback"""

    secret: int = 7

    guess: int = int(input("Guess a number: "))
    print("Your guess was " + str(guess))

    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif guess > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    else:
        print("How did you get this response???????")
    return None


if __name__ == "__main__":
    guess_a_number()
