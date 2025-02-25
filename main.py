import sys
from stats import get_total_words
from stats import get_num_chars
from stats import get_sorted_char_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_total_words(text)
    chars_dict = get_num_chars(text)
    chars_sorted_list = get_sorted_char_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

    
main()