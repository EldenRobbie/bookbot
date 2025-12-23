def word_count(document):
    words = document.split()
    return len(words)


def character_counter(document):
    characters = {}
    lowered_string = document.lower()
    for letter in lowered_string:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1

    return characters