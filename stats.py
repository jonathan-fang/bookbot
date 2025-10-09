def book_text_to_word_count(filepath):
    with open(filepath) as f:
        # turn filepath to string
        file_contents = f.read()
    # use .split method to count number of words
    words = file_contents.split()
    # return number of words as integer
    return len(words)

# addition to make sure characters and space counts, getting it checked by boots
def book_text_to_char_count(filepath):
    with open(filepath, "r") as f:
        # you can stack object methods like this too
        text = f.read().lower()
    # initialize empty dictionary
    char_dict = {}
    for ch in text:
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    return char_dict

def char_dict_to_sorted_list(char_dict):
    # input char_dict
    # list of dictionaries
    list_of_dicts = []
    for char in char_dict:
        # create tiny dictionary for each character value pair
        small_char_dict = {} # init
        # add key value pairs to small_char_dict
        small_char_dict["char"] = char
        # start with trying to make the whole function work then make helper functions?
        small_char_dict["num"] = char_dict[char]
        list_of_dicts.append(small_char_dict)
        # if char.isalpha(): # only include alphanumeric characters
    # output sorted list of dictionaries
    list_of_dicts.sort(reverse=True, key=find_num_key)
    return list_of_dicts

def find_num_key(char_dict):
    # helper function
    # input char_dict and key
    return char_dict["num"]