user_input = str(input())

    validated_str = ""
for letter in user_input:
    if letter.isalpha():
        validated_str += letter
print(validated_str)