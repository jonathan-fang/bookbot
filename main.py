from stats import book_test_to_word_count

def get_book_text(filepath):
    # from 4.2.3 currently inactive
    # intakes filepath
    with open(filepath) as f:
        file_contents = f.read()
    # output returns contents of file as string
    return file_contents

def main():
    print(f"Found {book_test_to_word_count('books/frankenstein.txt')} total words")

if __name__ == '__main__':
    main()