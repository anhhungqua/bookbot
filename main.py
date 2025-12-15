import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
from stats import get_num_words
from stats import get_num_unique_words
from stats import get_unique_characters_list_sort
def main():
    book_text = get_book_text(filepath)
    words_count = get_num_words(book_text)
    unique_words_count = get_num_unique_words(book_text)
    unique_characters_list_sort = get_unique_characters_list_sort(unique_words_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in unique_characters_list_sort:
        print(f"{item["char"]}: {item["num"]}")
main()