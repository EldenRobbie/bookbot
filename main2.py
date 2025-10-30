import sys
from stats import word_counter, char_counter, dict_to_sorted_list 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    word_count = word_counter(file_content)
    character_count = char_counter(file_content)
    sorted_list = dict_to_sorted_list(character_count)
    report(file_path, word_count)
    for letter in sorted_list:
        if not letter["letter"].isalpha():
            continue
        print(f"{letter['letter']}: {letter['number']}")
    print("============= END ===============")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def report(file_path, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    

main()