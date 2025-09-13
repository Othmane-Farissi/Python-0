from ft_filter import ft_filter
import sys


def is_bigger(word, n):
    """
    Check if the given word is longer than a specified length.

    Args:
        word (str): The word to check.
        n (int): The threshold length.

    Returns:
        bool: True if the length of word is greater than n, False otherwise.
    """
    return n < len(word)


def main():
    """
    Main function of the script.

    - Validates command-line arguments (expects exactly 2:
        a phrase and an integer).
    - Splits the phrase into words.
    - Filters words that are longer than the given
        integer using ft_filter().
    - Prints the filtered list of words.

    Raises:
        AssertionError: If the number of arguments is incorrect
        or if n is not a digit.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Bad arguments")
        phrase, n = sys.argv[1], sys.argv[2]

        if not n.isdigit():
            raise AssertionError("Bad arguments")

        n = int(n)

        phrase = phrase.split()

        filtered_words = ft_filter(lambda w: is_bigger(w, n), phrase)
        print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
