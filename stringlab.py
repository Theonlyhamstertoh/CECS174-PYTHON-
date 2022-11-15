def mirror_string(string):
  pass

def remove_letter_from_string(letter):
  pass

def char_num(string):
  #Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.
  pass

def any_char_num(letter):
  pass

def check_no_e(string):
  pass

def check_no_char(string, char):
  pass

def get_words_with_no_e(string):
  #compute percentage of words with no e
  # print words with no e
  pass

def avoids(word, forbidden_letters):
  # return True if words doesn't use any forbidden letters
  # prompt user to enter a string of forbidden letters
  pass

def uses_only(word, letters):
  # return True if word contains only letters in list
  pass

def is_abcedarian(words):
  # words appear in alphabetical order
  pass


# HELP FUNCTIONS
def find(string: str, char: str, index = 0 ):
  # return index
  return string.find(char, index)

def is_sorted(string: str):
  # return true is string has words sorted in ascending order
  return list(string) == sorted(string)

def is_anagram(string1: str, string2: str): 
  # if the two string, sorted in alphabetical order is the same, then they are the same letters
  return sorted(string1) == sorted(string2)

def has_duplicates(string: str):
  validated_str = string.replace(' ', ' ')
  # SET will remove any duplicate. 
  # if SET length != original string length, then FALSE
  return len(validated_str) == len(set(validated_str))    


def remove_duplicates(string: str):
  no_dupe: list = list(dict.fromkeys(string.replace("", "")))
  # join list together on empty string
  return "".join(no_dupe)


