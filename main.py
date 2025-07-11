def main():
    file_path = "books/frankenstein.txt"
    words = word_count(get_book_text(file_path))
    print(f"{words} words found in the document")


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)



main()