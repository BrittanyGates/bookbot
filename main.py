import sys
from stats import count_words
from stats import count_characters
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])

    total_words = count_words(text)
    character_count = count_characters(text)
    sorted_dict = sort_dict(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for character in sorted_dict:
        if not character["char"].isalpha():
            continue
        else:
            print(f"{character['char']}: {character['num']}")

    print("============= END ===============")


main()
