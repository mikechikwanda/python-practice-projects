# Cost of one Coke bottle
cost = 50

# Accepted coin denominations
valid_coins = [25, 10, 5]

# Initialize amount due
amount_due = cost

while amount_due > 0:
    # Prompt user for coin input
    coin_input = input("Insert Coin: ")

    # Check if the input is a valid integer
    if not coin_input.isdigit():
        print("Invalid input. Please insert a valid coin (5, 10, or 25).")
    else:
        # Convert input to an integer
        coin = int(coin_input)

        # Check if the inserted coin is valid
        if coin in valid_coins:
            # Deduct the coin value from the amount due
            amount_due -= coin
        else:
            print("Invalid coin. Please insert a valid coin (5, 10, or 25).")

    # Display the current amount due, even if the input was invalid
    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

# Calculate and output change owed if there's any overpayment
change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")
