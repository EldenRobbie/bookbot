from stats import word_count, character_counter

def main():
    content = "books/frankenstein.txt"
    book = get_book_text(content)
    ch_count = character_counter(book)
    print(f"Found {word_count(book)} total words")
    print(ch_count)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents




main()