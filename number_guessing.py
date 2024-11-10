"""Random modules help to generate a random number within specicifed range
   with random.randint(start of range, end f range)

    Returns:
        this will return an integer as the type enforced in the input is of int
"""

import random

# Number Guessing Game
# This program generates a random number between 1 and 100 and asks the player to guess it.
# Feedback is provided after each guess to guide the player towards the correct number.
# The game counts the number of attempts taken and congratulates the player upon success.


def get_user_guess():
    """
    Prompt the user to enter an integer guess.

    Returns:
        int: The user's guess as an integer.

    Raises:
        ValueError: If the user input is not an integer, prompts the user to enter a valid integer.
    """
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            return user_guess
        except ValueError:
            print("Please enter a valid integer")  # Inform user of invalid input


def main():
    """
    Main function to run the Number Guessing Game.

    The game generates a random number between 1 and 100, then prompts the user to guess the number.
    It provides feedback on each guess (too low, too high, or close) and counts the attempts taken.
    The game continues until the user guesses the correct number.
    """
    print("Welcome to the Number Guessing Game")
    print("I have selected a number between 1 and 100. Guess the number")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    count = 0  # Initialize attempt counter

    while True:
        # Get user's guess
        user_guess = get_user_guess()
        count += 1  # Increment the attempt count with each guess

        # Check if the guess is within the valid range (1 to 100)
        if user_guess in range(1, 100 + 1):

            # Check if the guess is correct
            if user_guess == number_to_guess:
                print("Bull's eye! Your guess is correct!!")
                print(
                    f"It took you {count} attempts"
                )  # Display number of attempts taken
                break  # End game when the correct guess is made

            # Provide feedback if the guess is close (within 2 units)
            elif abs(number_to_guess - user_guess) <= 2:
                print("So close!")

            # Provide feedback if the guess is too low
            elif user_guess < number_to_guess:
                print("Too low!")

            # Provide feedback if the guess is too high
            else:
                print("Too high!")

        else:
            # Inform the user if the guess is out of range
            print(
                "Your guess is out of the allowed range. Please guess a number between 1 and 100."
            )


# Run the main function to start the game
main()
