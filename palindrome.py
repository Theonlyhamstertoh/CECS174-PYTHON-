user_string = "never odd or even"


def palindrome(string):
    string = string.replace(" ", "")
    reversed_str = ""
    for x in reversed(string):
        reversed_str += x
    print(reversed_str)

    if reversed_str == string:
        return print(f"{user_string} is a palindrome")
    else:
        return print(f"{user_string} is not a palindrome")


(palindrome(user_string.lower()))
