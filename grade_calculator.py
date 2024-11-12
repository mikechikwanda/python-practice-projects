def get_user_score():
    """Prompts the user for a score and returns a valid score as an integer between 0 and 100."""
    while True:  # Loop until the user enters a valid score
        try:
            user_score = int(input("Enter your score (0-100): "))
            if 0 <= user_score <= 100:
                return user_score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Score must be an integer. Please try again.")


def main():
    student_score = get_user_score()

    # Determine the grade based on the score
    if student_score >= 90:
        print("A")
    elif student_score >= 80:
        print("B")
    elif student_score >= 70:
        print("C")
    elif student_score >= 60:
        print("D")
    else:
        print("F")


# Run the main function
main()
