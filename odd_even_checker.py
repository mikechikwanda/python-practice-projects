"""
Odd or Even Checker
This program prompts the user to input a number, then determines whether the 
number is odd, even, or zero. It provides appropriate feedback and handles 
invalid inputs gracefully.
"""


def get_number_from_user():
    """Prompt the user for a number, ensuring a valid integer is entered.

    Returns:
        int: The number provided by the user.
    """
    while True:
        try:
            user_number = int(input("Enter a number: "))
            return user_number
        except ValueError:
            print("Please enter a valid integer.")


def check_odd_even_or_zero(number):
    """Check if the number is odd, even, or zero and print the result.

    Args:
        number (int): The number to be checked.
    """
    if number == 0:
        print("The number is zero.")
    elif number % 2 == 0:
        print(f"Your number {number} is even.")
    else:
        print(f"Your number {number} is odd.")


def main():
    """Main function to execute the program's flow."""
    user_number = get_number_from_user()
    check_odd_even_or_zero(user_number)


# Run the main function
if __name__ == "__main__":
    main()
