from stats import get_book_text, get_and_count_words, count_characters

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    words = get_and_count_words(book_text)
    print(f"{words} words found in the document")
    number_of_characters = count_characters(book_text)
    print(number_of_characters)

main()