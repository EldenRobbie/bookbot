def word_count(text):
    words = text.split()
    return len(words)

# take text from the book as a string, and
# return the number of times each character,
# (including symbols and spaces) appear in the string

def character_counter(text):
    characters = text.lower()
    character_dict = {}
    for character in characters:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict