def main():
    num_words()

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def num_words():
    with open("books/frankenstein.txt") as f:
        number = 0
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            number += 1
        
        print(f"{number} words found in the document")


main()