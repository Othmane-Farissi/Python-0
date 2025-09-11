import sys

def get_input():
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

    punc = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    return c in punc

def main():

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
