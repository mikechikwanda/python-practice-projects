"""## 8. **Palindrome Checker**
   - Ask the user to input a word or phrase.
   - Check if the input is a palindrome (reads the same backward and forward).
   - Ignore spaces and capitalization when checking.
"""


def get_word_from_user() -> str:
    """Function prompts user for the word or phases they would like to check if palindrome or not"""
    while True:
        try:
            word = input("Enter word: ").strip().lower()
            if word.isalpha() == True:
                return word
            else:
                print("Please enter a valid word or phrase")
        except Exception as e:
            print(e)


def main():
    word_to_check = get_word_from_user()

    # reverse the word to check its exactly the same in reverse
    reversed_word = word_to_check[::-1]

    if word_to_check == reversed_word:
        print(f"{word_to_check} is a palindrome")
    else:
        print(f"{word_to_check} is not a palindrom")


if __name__ == "__main__":
    main()
