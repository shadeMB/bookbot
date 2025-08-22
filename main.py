def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(filepath):
    print(get_book_text(filepath))

main('books/frankenstein.txt')