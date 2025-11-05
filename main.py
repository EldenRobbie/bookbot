def main():
    path_to_file = "books/frankenstein.txt"
    print(get_book_text(path_to_file))


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

main()