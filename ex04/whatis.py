import sys

try:
    if len(sys.argv) == 2:
        num = int(sys.argv[1])

        if num % 2 == 0:
            print("I'm EVEN!")
        else:
            print("I'm ODD!")
    else:
        raise ValueError("one argument must be provided")
except ValueError as e:
    print(f"ERROR : {e}")

