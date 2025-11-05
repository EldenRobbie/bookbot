from stats import word_counter, number_dict


def main():
    path_to_file = "books/frankenstein.txt"
    file_content = get_book_text(path_to_file)
    num_words = word_counter(file_content)
    num_dict = number_dict(file_content)
    print(f"Found {num_words} total words")
    print(num_dict)



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

main()