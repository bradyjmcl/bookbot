def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    counter = 0
    for word in get_book_text(text).split():
        counter += 1
    return counter

def count_chars(file):
    char_dict = {}
    book_text = get_book_text(file).lower()
    for char in book_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def dict_sorter(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[0]))
