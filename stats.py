def book_test_to_word_count(filepath):
    with open(filepath) as f:
        # turn filepath to string
        file_contents = f.read()
    # use .split method to count number of words
    words = file_contents.split()
    # return number of words as integer
    return len(words)