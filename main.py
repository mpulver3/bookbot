from stats import get_num_words
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    file_name = sys.argv[1]
    get_num_words(file_name)
    return 

main()  
