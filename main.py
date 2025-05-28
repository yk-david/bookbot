import sys
from stats import count_number_of_words
from stats import count_number_of_characters
from stats import get_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    number_of_characters = count_number_of_characters(get_book_text(sys.argv[1]))
    sorted_list = get_report(number_of_characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_number_of_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")

    for character_dict in sorted_list:
        print(f"{character_dict["char"]}: {character_dict["num"]}")
    
    print("============= END ===============")
    

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
        return file_contents


main()
