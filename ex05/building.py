import sys

def isUpper(c):
    return c.isupper()

def isLower(c):
    return c.islower()

def isDigit(c):
    return c.isdigit()

def isMark(c):
    punctuation_chars = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    return c in punctuation_chars

def isSpace(c):
    return c.isspace()

def get_input():
    if len(sys.argv) == 1:
        text = input("Please enter a string: ")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        raise AssertionError("Only one argument is allowed!")
    return text

def main():
    text = get_input()

    a = b = c = d = e = 0  # counters: upper, lower, punctuation, spaces, digits

    for char in text:
        if isUpper(char):
            a += 1
        elif isLower(char):
            b += 1
        elif isDigit(char):
            e += 1      # digits
        elif isMark(char):
            c += 1      # punctuation
        elif isSpace(char):
            d += 1      # spaces

    print(f'The text contains {len(text)} characters:')
    print(f'{a} upper letters')
    print(f'{b} lower letters')
    print(f'{c} punctuation marks')
    print(f'{d} spaces')
    print(f'{e} digits')

if __name__ == "__main__":
    main()
