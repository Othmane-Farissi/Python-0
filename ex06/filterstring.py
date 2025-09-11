from ft_filter import ft_filter
import sys

def is_bigger(word, n):
    return n < len(word)

def main():

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
