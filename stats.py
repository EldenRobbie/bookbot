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