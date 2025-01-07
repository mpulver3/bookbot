def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()
        #print(file_contents)
        number_of_words = word_count(file_contents)
        char_dict = char_count(file_contents)
        #print(f"{number_of_words} is the number of words in the book.")
        #print(f"{char_dict} is the directory of characters used.")
        report(file_name, number_of_words, char_dict)
    return 
        
def char_count(book_string):
    count_dict = {}
    book_string_low = book_string.lower()
    for i in range(0, len(book_string_low)):
        if book_string_low[i] in count_dict:
            count_dict[f"{book_string_low[i]}"] += 1
        else:
            count_dict[f"{book_string_low[i]}"] = 1 
    return count_dict

def word_count(book):
    list_of_words = book.split()
    count = 0
    for w in list_of_words:
        count += 1
    return count

def report(file_name, num_words, char_totals):

  print(f"--- Begin report of {file_name} ---")
  print(f"{num_words} words fount in the document \n")
  
  print("--- End report ---")
  return 

main()
