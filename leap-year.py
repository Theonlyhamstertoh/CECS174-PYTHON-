# Define your function here.
def days_in_feb(user_year):
    # check that it is a century year by being divisible by 400
    if user_year % 400 == 0 and user_year % 100 == 0 or not user_year % 100 == 0 and user_year % 4 == 0:
        return 29
        # return f"{int(user_year)} has 29 days in February."
    return 28
    # return f"{int(user_year)} has 28 days in February. "

    # output days in feb + 1


if __name__ == '__main__':
    print(f"{int(120)} has {days_in_feb(int(input()))} days in February. ")
    # Type your code here. Your code must call the function.