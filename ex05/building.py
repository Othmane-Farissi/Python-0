import sys


def get_input():
    """
    Retrieve input text from command-line arguments or user prompt.

    Returns:
        str: The input text provided either as an argument or via stdin.

    Raises:
        AssertionError: If more than one argument is provided.
        SystemExit: If an error occurs, exits the program with code 1.
    """
    try:
        if len(sys.argv) == 1:
            text = input("Please enter a string: ")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("Number of arguments must be 1!")
        return text
    except AssertionError as e:
        print(f"ERROR: {e}")
        sys.exit(1)


def isMark(c):
    """
    Check if a given character is a punctuation mark.

    Args:
        c (str): A single character to check.

    Returns:
        bool: True if the character is a punctuation mark, False otherwise.
    """
    punc = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    return c in punc


def main():
    """
    Main function of the program.

    - Retrieves input text (from args or prompt).
    - Iterates through characters and counts:
        * Uppercase letters
        * Lowercase letters
        * Digits
        * Spaces
        * Punctuation marks
    - Prints a summary of the character counts.
    """
    text = get_input()
    up = lo = pu = sp = di = 0

    for i in range(len(text)):
        if text[i].isdigit():
            di += 1
        elif text[i].isupper():
            up += 1
        elif text[i].islower():
            lo += 1
        elif text[i].isspace():
            sp += 1
        elif isMark(text[i]):
            pu += 1

    print(f'The text contains {len(text)} characters:')
    print(f'{up} upper letters')
    print(f'{lo} lower letters')
    print(f'{pu} punctuation marks')
    print(f'{sp} spaces')
    print(f'{di} digits')


if __name__ == "__main__":
    main()
