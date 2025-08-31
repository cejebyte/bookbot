import sys
from stats import get_num_words
from stats import char_count
from stats import sort_on
from stats import get_book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    counts = char_count(text)
    result = sort_on(counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    total = get_num_words(text)
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    for item in result:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
