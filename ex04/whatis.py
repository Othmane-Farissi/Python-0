import sys

if len(sys.argv) > 1:
    num = int(sys.argv[1])
    if (num % 2) == 0:
        print("I'M EVEN")
    else:
        print("I'M ODD")