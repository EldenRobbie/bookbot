from stats import (
    get_num_words,
    char_dict,
    chars_dict_to_sorted_list,
)

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    c_num = char_dict(text)
    num_words = get_num_words(text)
    chars_sorted_list = chars_dict_to_sorted_list(c_num)
    print_report(filepath, num_words, chars_sorted_list)

def get_book_text(file_path):  
    with open(file_path) as f:
        return f.read()

def print_report(filepath, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()