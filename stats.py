def num_words():
    with open("books/frankenstein.txt") as f:
        number = 0
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            number += 1
        
        return f"{number} words found in the document"


def character_counter():
    with open("books/frankenstein.txt") as f:
        my_dict = {}
        file_contents = f.read()
        my_dict = {}
        symbols = list(file_contents.lower())
        for symbol in symbols:
            if symbol not in my_dict:
                my_dict[symbol] = 1
            else:
                my_dict[symbol] += 1
        return my_dict
