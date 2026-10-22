#!/usr/bin/env python3

# Created by: VovaM
# Created on: 22 Oct 2026
# This program is a number guessing game that handles non-integer input.

import random


def main():
    # Generate a random number between 0 and 9
    secret_number = random.randint(0, 9)

    # Get input from the user
    user_input_string = input("Guess a number between 0 and 9: ")

    # Try to convert input to integer and check the guess
    try:
        user_input_integer = int(user_input_string)

        if user_input_integer == secret_number:
            print("You guessed correctly!")
        else:
            print(f"Wrong guess! The correct number was {secret_number}.")
    except ValueError:
        print(f"{user_input_string} is not an integer.")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
