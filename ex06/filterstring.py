import sys
from ft_filter import ft_filter   # ✅ correct way to import from ft_filter.py

def get_input():
    if len(sys.argv) != 3:
        raise AssertionError("The arguments are bad")

    try:
        arg1 = int(sys.argv[1])
    except ValueError:
        raise AssertionError("The arguments are bad")

    arg2 = sys.argv[2]
    if not isinstance(arg2, str) or arg2.strip() == "":
        raise AssertionError("The arguments are bad")

    return arg1, arg2

def isBigger(word, n):
    """Return True if word length is greater than n"""
    return len(word) > n

def main():
    arg1, arg2 = get_input()

    # Split string into words
    words = arg2.split()

    # Use ft_filter with lambda to pass the threshold
    filtered_words = ft_filter(lambda w: isBigger(w, arg1), words)

    print(list(filtered_words))


if __name__ == "__main__":
    main()
