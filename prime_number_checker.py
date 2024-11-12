import math


def get_user_num():
    """Function prompts user for the number they would like to check if prime.

    Returns:
        int: The number entered by the user.
    """
    while True:
        try:
            num = int(input("Enter number: "))
            return num
        except ValueError:
            print("Not a valid number. Please enter an integer.")


def main():
    """Main function checking if the number is prime or not."""
    while True:
        num = get_user_num()
        if num <= 1:
            print("Number must be greater than 1.")
        else:
            is_prime = True  # Assume number is prime initially.
            for i in range(2, int(math.sqrt(num)) + 1):  # Only check up to sqrt(num).
                if num % i == 0:
                    is_prime = False
                    print(f"{num} is not a prime number. It is divisible by {i}.")
                    break

            if is_prime:
                print(f"{num} is a prime number.")


if __name__ == "__main__":
    main()
