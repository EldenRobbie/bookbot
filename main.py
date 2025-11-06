import sys
from stats import word_counter, number_dict, chars_to_dict_sorted_list

# Remove any hardcoded paths from your code

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]
    file_content = get_book_text(path_to_file)
    num_words = word_counter(file_content)
    num_dict = number_dict(file_content)
    sorted_list = chars_to_dict_sorted_list(num_dict)
    intro(path_to_file, num_words)
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def intro(file_path, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

main()