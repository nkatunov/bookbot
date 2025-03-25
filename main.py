from stats import get_num_words, get_characters_sorted, format_char_message
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

# Get book text as a string
def get_book_text(filepath):
        content = ""
        with open(filepath) as f:
            content += f.read()
        return content

def main():
        book = get_book_text(path)
        number_of_words = get_num_words(book)
        characters_count = get_characters_sorted(book)
        formatted_char_message = format_char_message(characters_count)
        message_one = f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n"
        message_two = f"----------- Word Count ----------\nFound {number_of_words} total words\n"
        message_three = f"--------- Character Count -------\n{formatted_char_message}"
        message_four = "============= END ==============="

        print(message_one, message_two, message_three, message_four)
        # print(sort_dict(characters_count))

main()
