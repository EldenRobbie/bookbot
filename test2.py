def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return ""
    
    
def words_number():
    num = get_book_text("books/frankenstein.txt")
    numb = len(num.split())
    return numb


def character_counter():
    lower_case = (get_book_text("books/frankenstein.txt")).lower()
    
