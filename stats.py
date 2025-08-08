def get_num_words(file_path):
    number = 0
    file = file_path.split()
    for f in file:
        number += 1
    return number

def char_dict(text):
    char_dicts = {}
    for t in text.lower():
        if t in char_dicts:
            char_dicts[t] += 1
        else:
            char_dicts[t] = 1
    return char_dicts

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    return sorted_list