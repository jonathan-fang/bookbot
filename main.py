import sys
from stats import book_text_to_word_count, book_text_to_char_count, char_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {book_text_to_word_count(filepath)} total words")
    print("--------- Character Count -------")
    for item in char_dict_to_sorted_list(book_text_to_char_count(filepath)):
        if item['char'].isalpha(): # only include alphanumeric characters
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == '__main__':
    main()