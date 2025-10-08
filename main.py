def get_book_text(filepath):
    # intakes filepath
    with open(filepath) as f:
        file_contents = f.read()
    # output returns contents of file as string
    return file_contents

def book_test_to_word_count(filepath):
    with open(filepath) as f:
        # turn filepath to string
        file_contents = f.read()
    # use .split method to count number of words
    words = file_contents.split()
    # return number of words as integer
    return len(words)

def main():
    # print(get_book_text('books/frankenstein.txt'))
    print(f"Found {book_test_to_word_count('books/frankenstein.txt')} total words")

if __name__ == '__main__':
    main()