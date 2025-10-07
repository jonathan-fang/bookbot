def get_book_text(filepath):
    # intakes filepath
    with open(filepath) as f:
        file_contents = f.read()
    # output returns contents of file as string
    return file_contents

def main():
    print(get_book_text('books/frankenstein.txt'))

main()