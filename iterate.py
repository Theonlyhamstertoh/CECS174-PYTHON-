# ''' Type your code here. '''
# start = int(input())
# end = int(input())
# print_string = str(start)

# if start > end:
#     print("Second integer can't be less than the first.")
# else:
#     while start < end - (end % 5):
#         start += 5
#         print_string += f" {start}"
#     print(print_string)
''' SAME DIGIT COUNTDOWN '''
# endCount = int(input())
# same_digits = False
# if 11 <= endCount <= 100:
#     # keep looping as long as sameDigit is false
#     while same_digits == False:
#         split_num = (list(str(endCount)))
#         print(endCount)
#         if split_num[0] == split_num[1]:
#             same_digits = True
#         endCount -= 1
# else:
#     print("Input must be 11-100")
'''PERFECT SQUARE'''
# import math

# val = int(input())
# while math.sqrt(val) % 1 != 0:
#     val = int(input())

# print(int(math.sqrt(val)))
''' BIGGIE SMALLS '''
# # read 10 integers by using a for loop
max_value = int(input())
min_value = float('inf')

for i in range(0, 3):
    user_input = int(input("Input Num:"))
    if max_value < user_input:
        max_value = user_input
    if user_input < min_value:
        min_value = user_input

print(min_value, max_value)
