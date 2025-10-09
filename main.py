from stats import book_text_to_word_count, book_text_to_char_count, char_dict_to_sorted_list

def get_book_text(filepath):
    # from 4.2.3 currently inactive
    # intakes filepath
    with open(filepath) as f:
        file_contents = f.read()
    # output returns contents of file as string
    return file_contents

def pretty_report():
    pass

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_text_to_word_count('books/frankenstein.txt')} total words")
    print("--------- Character Count -------")
    for item in char_dict_to_sorted_list(book_text_to_char_count('books/frankenstein.txt')):
        if item['char'].isalpha(): # only include alphanumeric characters
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == '__main__':
    main()