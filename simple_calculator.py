"""
Simple Calculator
This program prompts the user to input two numbers and an arithmetic operation (+, -, *, /).
It then performs the corresponding calculation and outputs the result.
Division by zero is handled gracefully with an error message.
"""


def get_integer(prompt):
    """Prompt the user for an integer input and handle invalid entries.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        int: The valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def calculate(first_number, second_number, operation):
    """Perform a calculation based on the provided operation.

    Args:
        first_number (int): The first operand.
        second_number (int): The second operand.
        operation (str): The operation to perform (+, -, *, /).

    Returns:
        str: The result of the calculation or an error message if the operation is invalid.
    """
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        try:
            return first_number / second_number
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Unsupported operation. Please use +, -, *, or /."


def main():
    """Main function to run the calculator program."""
    first_number = get_integer("Enter the first number: ")
    second_number = get_integer("Enter the second number: ")
    operation = input("Choose an operation (+, -, *, /): ")

    result = calculate(first_number, second_number, operation)
    print(f"Result: {result}")


# Run the main function
if __name__ == "__main__":
    main()
