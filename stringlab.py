quote = '''Out of the night that covers me, Black as the pit from pole to pole, I thank whatever gods may be For my unconquerable soul. In the fell clutch of circumstance I have not winced nor cried aloud. Under the bludgeonings of chance My head is bloody, but unbowed. Beyond this place of wrath and tears Looms but the Horror of the shade, And yet the menace of the years Finds and shall find me unafraid. It matters not how strait the gate, How charged with punishments the scroll, I am the master of my fate, I am the captain of my soul.'''

# HELP FUNCTIONS
def find(string: str, char: str, index = 0 ):
  # return index
  return string.find(char, index)

def is_sorted(string: str):
  # return true is string has char sorted in ascending order
  return list(string) == sorted(string)

def is_anagram(string1: str, string2: str): 
  # if the two string, sorted in alphabetical order is the same, then they are the same letters
  return sorted(string1) == sorted(string2)

def has_duplicates(string: str):
  validated_str = remove_whitespace(string)
  # SET will remove any duplicate. 
  # if SET length != original string length, then FALSE
  return len(validated_str) == len(set(validated_str))    


def remove_duplicates(string: str):
  no_dupe: list = list(dict.fromkeys(remove_whitespace(string)))
  # join list together on empty string
  return "".join(no_dupe)


def remove_whitespace(string: str):
  return string.replace(' ', '')








def mirror_string(string):
  reverse_str = string[::-1]
  return f"{string}---{reverse_str}"

def remove_letter_from_string(string: str, letter: str):
  return string.replace(letter, "")

def char_e_num(string):
  validated_str = remove_whitespace(string)
  str_length = len(validated_str)
  e_count = validated_str.count("e")
  percent = e_count/str_length * 100

  return f"Your text contains {str_length} alphabetic characters, of which {e_count} {percent:.1f}% are 'e'."



def any_char_num(string: str, letter: str):
  validated_str = remove_whitespace(string)
  str_length = len(validated_str)
  char_count = validated_str.count(letter)
  percent = char_count/str_length * 100

  return f"Your text contains {str_length} alphabetic characters, of which {char_count} {percent:.1f}% are '{letter}'."

def check_no_e(string: str):
  return True if string.find('e') == -1 else False


def check_no_char(string: str, char: str):
  return True if string.find(char) == -1 else False

def get_words_with_no_e(string: str):
  word_lists = string.split(' ')
  no_e_list = []
  for word in word_lists:
    if word.find("e") == -1:
      no_e_list.append(word)
    
  percentage = len(no_e_list) / len(word_lists) * 100
  return f"\n\t({percentage:.1f}% of words without e) " + " ".join(no_e_list) 
  #compute percentage of words with no e
  # print words with no e
  pass


def avoids(string: str, forbidden_letters: str):
  # return True if words doesn't use any forbidden letters
  # prompt user to enter a string of forbidden letters

  # forbidden_letters = input("Enter Forbidden Letters: ")
  for letter in forbidden_letters:
    if letter in string:
      return False
  
  return True

def uses_only(string, only_letters):
  # return True if word contains only letters in list
  for letter in string:
    if letter not in only_letters:
      return False
  return True
  
def uses_all(string, required_letters):
  for letter in required_letters:
    if letter not in string:
      return False
  return True

  # uses all required letters at least once
def is_abcedarian(string: str):
  # words appear in alphabetical order
  return is_sorted(string)



print("is_abcedarian('Weibo') ==", is_abcedarian('weibo'))
print("uses_all('weibo', 'abc') ==", uses_all('weibo', 'abc'))
print("uses_all('weibo', 'bow') ==", uses_all('weibo', 'bow'))
print("uses_only('weibo', 'jeff') ==", uses_only('weibo', 'jeff'))
print("avoids('weibo', 'z') ==", avoids('weibo', "z"))
print("get_words_with_no_e('weibo zhang'):", get_words_with_no_e('weibo zhang'))
print("check_no_char('weibo zhang', 'u') ==", check_no_char('weibo zhang', 'u'))
print("check_no_e ==", check_no_e('weibo zhang'))
print("remove_letter_from_string('weibo zhang', 'e') ==", remove_letter_from_string('weibo zhang', 'e'))