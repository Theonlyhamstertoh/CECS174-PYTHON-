from math import pow

# Get the user input and convert the input string to type integer
num1 = int(input("Input your first integer: \n"))
num2 = int(input("Input your Second integer: \n"))

# Print out the equations and results of the two given input
# F-string allow to format the string to input variables and expressions
print(
    f"value #1 = {num1}",
    f"value #2 = {num2}",
    f"The addition is:         {num1:>5} + {num2} = {num1 + num2}",
    f"The subtraction is:      {num1:>5} - {num2} = {num1-num2}",
    f"The multiplication is:   {num1:>5} * {num2} = {num1*num2}",
    f"The division is:         {num1:>5} / {num2} = {num1/num2:.2f}",  # result is rounded to two decimals
    f"The integer division is: {num1:>5} // {num2} = {num1 // num2}",
    f"The modulo is:           {num1:>5} % {num2} = {num1 % num2}",
    f"The exponent is:         {num1:>5} ^ {num2} = {pow(num1, num2):.0f}",  # result is rounded to whole number
    sep="\n",
)
