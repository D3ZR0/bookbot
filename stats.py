def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_and_count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    letters = {}
    for letter in book_text:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters