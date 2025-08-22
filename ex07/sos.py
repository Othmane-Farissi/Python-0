import sys

def isPun(c):
    punctuation_chars = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    return c in punctuation_chars

def get_input():
    if len(sys.argv) != 2:
        raise AssertionError("bad arguments")

    s = sys.argv[1]
    # Check if the string contains punctuation
    for c in s:
        if isPun(c):
            raise AssertionError("bad arguments")
    return s

def convert(s):
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
    for char in s.upper():
        if char in MORSE_CODE:
            ret.append(MORSE_CODE[char])
        else:
            raise AssertionError(f"Unsupported character: {char}")
    return " ".join(ret)

def main():
    s = get_input()
    morse = convert(s)
    print(morse)

if __name__ == "__main__":
    main()
