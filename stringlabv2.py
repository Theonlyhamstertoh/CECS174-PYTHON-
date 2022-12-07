mobySmallFile = open('./mobysmall.txt', "r")
mobySmallTxt = mobySmallFile.read()


# PART 1 -----------------------------------------------------------------
def numChar(word):  #Return number of characters

  count = 0
  for i in word:
    count += 1
  return count


def lastChar(word):  #Return the last character in the string
  return word[-1:]


def charE(
  word
):  # Return the location of the first occurence of the letter "e" (0 if not found)
  for i in word:
    if i == "e":
      x = word.index(i)
      return x
  return 0


def numWords(word):  #Return number of words without space or tab
  count = 1
  for i in word:
    if i == " " or i == '\t':
      count += 1
  return count


def firstName(word):  #Return first name
  for i in word:
    if i == " ":
      return (word[0:word.index(i)])


def numVowels(word):  #Return number of vowels
  vowels = ("a", "e", "i", "o", "u")
  count = 0
  for i in word:
    if i in vowels:
      count += 1
  return count


# def capVowels(word):  #Return word with capitalized vowels
#   vowels = ("a", "e", "i", "o", "u")
#   new = " "
#   for i in word:
#     if i in vowels:
#       new += i.upper()
#     else:
#       new += i
#   return new

# #Display the string centered between 50 ~~~~~ and 70 ++
# def centered(word):
#   curly = word.center(50, "~")
#   new_string = curly.center(70, "+")
#   return new_string

# #Display the string split in half on either end of 70 ***
# def half(word):
#   split = int(len(word) / 2)
#   return word[:split] + ("*" * 70) + word[split:]

# #################################################
# #Use string f{} format

# user_name = input("Please enter your name: ")

# #Print Statements
# print(f"\nYour name is {numChar(user_name)} characters long.")
# print(f"The last character is: {lastChar(user_name)}.")
# print(f"The first 'e' is at position {charE(user_name)}.")
# print(f"Your name has {numWords(user_name)} words.")
# print(f"Your first name is {firstName(user_name)}.")
# print(f"Your name contains {numVowels(user_name)} vowels.")
# print(f"Your name with uppercase vowels is: {capVowels(user_name)}")
# print(f"{centered(user_name)}")
# print(f"{half(user_name)}")

# PART 2 -----------------------------------------------------------------
quote = '''Out of the night that covers me, Black as the pit from pole to pole, I thank whatever gods may be For my unconquerable soul. In the fell clutch of circumstance I have not winced nor cried aloud. Under the bludgeonings of chance My head is bloody, but unbowed. Beyond this place of wrath and tears Looms but the Horror of the shade, And yet the menace of the years Finds and shall find me unafraid. It matters not how strait the gate, How charged with punishments the scroll, I am the master of my fate, I am the captain of my soul.'''


# HELP FUNCTIONS
def find(string: str, char: str, index=0):
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


# FUNCTIONS
def mirror_string(string):
  reverse_str = string[::-1]
  return f"{string}---{reverse_str}"


def remove_letter_from_string(string: str, letter: str):
  return string.replace(letter, "")


def char_e_num(string):
  validated_str = remove_whitespace(string)
  str_length = len(validated_str)
  e_count = validated_str.count("e")
  percent = e_count / str_length * 100

  return f"Your text contains {str_length} alphabetic characters, of which {e_count} or {percent:.1f}% are 'e'."


def any_char_num(string: str, letter: str):
  validated_str = remove_whitespace(string)
  str_length = len(validated_str)
  char_count = validated_str.count(letter)
  percent = char_count / str_length * 100

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


sep = "\n--------------------------------------------------------\n"


def log(description, value, file):
  print(description, value, end=sep)
  print(description, value, file=file, end=sep)


with open("./output.txt", "w") as my_file:
  log("check if no 'z' in file: ", check_no_char(mobySmallTxt, "z"), my_file)
  log("check if there is no e: ", check_no_e(mobySmallTxt), my_file)
  log("number of 'e' in file: ", char_e_num(mobySmallTxt), my_file)
  log("number of 'z' in file: ", any_char_num(mobySmallTxt, "z"), my_file)
  log("avoids using $: ", avoids(mobySmallTxt, "$"), my_file)
  log("uses characters 'abcdef'", uses_all(mobySmallTxt, "abcdef"), my_file)
  log("Get Words With No 'e'", get_words_with_no_e(mobySmallTxt), my_file)
  log("Mirror string", mirror_string(mobySmallTxt), my_file)
  log("remove 'e' from string", remove_letter_from_string(mobySmallTxt, "e"),
      my_file)

mobySmallFile.close()
