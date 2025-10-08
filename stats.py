def book_text_to_word_count(filepath):
    with open(filepath) as f:
        # turn filepath to string
        file_contents = f.read()
    # use .split method to count number of words
    words = file_contents.split()
    # return number of words as integer
    return len(words)

def book_text_to_char_count(filepath):
    # initialize char_dict as empty dictionary
    char_dict = {}
    # input: filepath to book as string
    with open(filepath) as f:
        file_contents = f.read()
    # split to get list of words
    words = file_contents.split()
    for word in words:
        for char in word:
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    # convert any character to lowercase using .lower() method
    # use a dictionary of string -> int
    # returns number of times each character including symbols and spaces appear in the string
    return char_dict