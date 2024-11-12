"""This app implements the popular fizzbuzz challenge in my own version
"""


def main():
    """This function runs the FizzBuzz sequence up to a user-specified limit.

    Prints "Fizz" for numbers divisible by 3, "Buzz" for numbers divisible by 5,
    "FizzBuzz" for numbers divisible by both, and the number itself otherwise.
    Additionally, counts and displays occurrences of "FizzBuzz".
    """
    num = get_user_number()
    count_fizzbuzz = 0

    for n in range(1, num + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
            count_fizzbuzz += 1
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

    print(f"There are {count_fizzbuzz} occurrences of 'FizzBuzz'.")


def get_user_number():
    """Prompts the user for a valid integer limit and returns it.

    Ensures that the input is a positive integer greater than zero.

    Returns:
        int: The user-specified upper limit for FizzBuzz.
    """
    while True:
        try:
            user_number = int(input("Enter a positive integer as the upper limit: "))
            if user_number < 1:
                print("Please enter a number greater than zero.")
            else:
                return user_number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# summarise the main fucntion for context
print(main.__doc__)

# start program
if __name__ == "__main__":
    main()
