"""this exercise i did it in cs50p 
"""


def main():
    coke_price = 50
    amount_due = coke_price  # Set initial amount due for a Coke
    accepted_coins = [25, 10, 5]  # List of accepted coin denominations

    while amount_due > 0:
        coin = int(input("Please insert coin: "))

        # Check if the inserted coin is in accepted denominations
        if coin in accepted_coins:
            amount_due -= coin  # Deduct coin value from amount due

            # Only display the amount due if there is still an outstanding balance
            if amount_due > 0:
                print(f"Amount due: {amount_due} cents")
        else:
            print("Invalid coin. Please use 25, 10, or 5 cents only.")

    # Calculate and display any change owed (if amount_due is negative)
    change = abs(amount_due)  # Amount due might be negative if overpaid
    if change > 0:
        print(f"Your change is {change} cent(s)")


if __name__ == "__main__":
    main()
