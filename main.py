import sys

from stats import get_word_count, get_character_count, sorted_list


def get_book_text(filepath):
      with open(filepath) as file:
            read_book = file.read()
      return read_book


def main():
      if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>") 
            sys.exit(1)  

      book_path = sys.argv[1]
      word_count = get_word_count(book_path)
      char_dict = get_character_count(book_path)
      sorted_chars = sorted_list(char_dict)
       

      print("============ BOOKBOT ============")
      print(f"Analyzing book found at {book_path}...")
      print("----------- Word Count ----------")
      print(f"Found {word_count} total words")
      print("--------- Character Count -------")
      for char_info in sorted_chars:
            char = char_info["char"]
            num = char_info["num"]
            if char.isalpha():
                  print(f"{char}: {num}")
      print("============= END ===============")

main()

