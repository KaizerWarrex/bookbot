import sys

def get_character_count(filepath):
            with open(filepath) as file:
                  read_book = file.read()
            character_count = char_counts_from_text((read_book.lower()))

            return character_count

def char_counts_from_text(text: str) -> dict:
      counts = {}
      for char in text:
            if char in counts:
                  counts[char] += 1
            else:
                  counts[char] = 1
      return counts


def get_word_count(filepath):
      with open(filepath) as file:
            read_book = file.read()
            word_count = len(read_book.split())
      return word_count


def sorted_list(chars: dict):
      characters = []

      for char, count in chars.items():
             characters.append({"char": char, "num": count})
      characters.sort(key=lambda x: x["num"], reverse=True)
      return characters 