from stats import word_count, character_counter


def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    words = word_count(text)
    print(f"{words} words found in the document")
    print(character_counter(text))


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents





main()