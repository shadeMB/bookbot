from stats import (
    get_num_words,
    get_num_characters,
    sort_char_dict
)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)             # get the book text
    num_words = get_num_words(text)             # find number of words in book text
    char_counts = get_num_characters(text)      # dict containing chars and the count for each one
    sorted_dict = sort_char_dict(char_counts)   # list of dicts containing the chars and the count for each one

    # print the full report
    print_report(book_path, num_words, sorted_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_dict:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

main()
