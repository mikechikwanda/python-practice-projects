"""app gets user input for email, splits it to determine user_name and domain 
"""


# get user input for email
def main():
    """This function splits email from user to determine username and domain seperately"""

    # split email into 2 parts using @ and validate input
    user_email = get_user_email()
    if "@" in user_email and user_email.count("@") == 1:
        split_email: list = user_email.split("@")
        first_name: str = split_email[0]
        domain: str = split_email[1]

        print(f"Username: {first_name}")
        print(f"Domain: {domain}")
    else:
        print("Invalid email format")


def get_user_email() -> str:
    """This function get user input for email

    Returns:
        str: representing user email
    """
    while True:
        user_email: str = input("Enter email: ").strip().lower()
        if user_email:
            return user_email
        print("Email cannot be empty. Please try again")


if __name__ == "__main__":
    main()
