def word_counter(file_content):
    words = file_content.split()
    return len(words)


def char_counter(file_content):
    char_dict = {}
    lowered_content = file_content.lower()
    for char in lowered_content:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["number"]

def dict_to_sorted_list(dict):
    sorted_list = []
    for letter in dict:
        sorted_list.append({"letter": letter, "number": dict[letter]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list