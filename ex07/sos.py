import sys

def convert(phrase):
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

    if len(sys.argv) != 2:
        raise AssertionError("bad arguments")
    s = sys.argv[1]
    converted = convert(s)
    print(f"{converted}")

if __name__ == "__main__":
    main()
