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
    counts = {}
    for ch in text:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts