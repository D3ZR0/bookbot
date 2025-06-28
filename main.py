from stats import get_book_text, get_and_count_words, count_characters, sort_characters, sort_on
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(path_to_file = sys.argv[1]) # "books/frankenstein.txt"
    words = get_and_count_words(book_text)
    number_of_characters = count_characters(book_text)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv [1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for letter in sort_characters(number_of_characters):
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
        else:
            pass
    print("============= END ===============")

main()