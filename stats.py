def word_counter(file_content):
    split_file = file_content.split()
    return len(split_file)


def number_dict(file_content):
    num_dict = {}
    lowered_content = file_content.lower()
    for letter in lowered_content:
        if letter not in num_dict:
            num_dict[letter] = 1
        else:
            num_dict[letter] += 1
    return num_dict


def sort_on(items):
    return items["num"]

def chars_to_dict_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list