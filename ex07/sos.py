import sys


def convert(phrase):
    """
    Convert a given phrase into Morse code.

    Each character is translated to its Morse code equivalent:
    - Letters (A–Z)
    - Digits (0–9)
    - Space → "/"

    Args:
        phrase (str): The input phrase to convert.

    Returns:
        str: A string containing the Morse code translation of the phrase,
             with each symbol separated by a space.

    Raises:
        AssertionError: If the phrase contains unsupported characters.
    """
    MORSE_CODE = {
        # Letters
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",

        # Numbers
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",

        # Space
        " ": "/"
    }

    ret = []
    for i in range(len(phrase)):
        c = phrase[i].upper()
        if c in MORSE_CODE:
            ret.append(MORSE_CODE[c])
        else:
            raise AssertionError("arguments are bad")

    return " ".join(ret)


def main():
    """
    Main function of the script.

    - Validates command-line arguments (expects exactly 1).
    - Converts the provided phrase into Morse code.
    - Prints the Morse code result.

    Raises:
        AssertionError: If the number of arguments is not exactly 1.
    """
    if len(sys.argv) != 2:
        raise AssertionError("bad arguments")
    s = sys.argv[1]
    converted = convert(s)
    print(f"{converted}")


if __name__ == "__main__":
    main()
