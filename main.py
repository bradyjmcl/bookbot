from stats import get_num_words, count_chars, dict_sorter
import sys

def main(file_path):
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_path)} total words")
    print("--------- Character Count -------")
    
    char_dict = count_chars(file_path)
    for char, count in dict_sorter(char_dict).items():
        if char.isalpha():
            print(f"{char}: {count}")

if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            main(sys.argv[1])
