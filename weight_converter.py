def user_option() -> int | None:
    """
    Displays a welcome message and prompts the user to select a conversion option.
    Returns:
        int or None: The user's choice (1 for kg to lbs, 2 for lbs to kg), or None if input is invalid.
    """
    print("Welcome to the Weight Converter App")
    try:
        option = int(
            input(
                "Please choose your action: \n1. Kilograms to Pounds\n2. Pounds to Kilograms\n"
            )
        )
        if option in (1, 2):
            return option
        print("Invalid option. Please choose 1 or 2.")
        return None
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None


def kilos_to_pounds(kilos: float) -> float:
    """Converts kilograms to pounds."""
    return kilos * 2.20462


def pounds_to_kilos(pounds: float) -> float:
    """Converts pounds to kilograms."""
    return pounds * 0.453592


def get_weight_input(unit: str) -> float | None:
    """
    Prompts the user to enter a weight and returns it as a float.
    Args:
        unit (str): The unit of weight ('kilograms' or 'pounds').
    Returns:
        float or None: The entered weight as a float, or None if input is invalid.
    """
    try:
        return float(input(f"Please enter weight in {unit}: "))
    except ValueError:
        print(f"Invalid input. Please enter a numeric value for {unit}.")
        return None


def main():
    while True:
        choice = user_option()
        if choice == 1:
            kilos = get_weight_input("kilograms")
            if kilos is not None:
                print(f"{kilos} kg is equal to {kilos_to_pounds(kilos):.2f} lbs")
        elif choice == 2:
            pounds = get_weight_input("pounds")
            if pounds is not None:
                print(f"{pounds} lbs is equal to {pounds_to_kilos(pounds):.2f} kg")
        if choice:
            again = (
                input("Would you like to perform another conversion? (y/n): ")
                .strip()
                .lower()
            )
            if again != "y":
                print("Thank you for using the Weight Converter App. Goodbye!")
                break


if __name__ == "__main__":
    main()
