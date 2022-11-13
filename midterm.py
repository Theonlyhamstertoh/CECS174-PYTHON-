# read 100 integer inputs
# count numbers of negative inputs
# count == number of negative integers
# no output
'''
i = 0
count = 0
while i < 3:
    num = int(input())
    if num < 0:
        count += 1
    i += 1

print('count', count)
'''

# Calculate Gallons
gas_price = float(input())
num_gal = float(input())


def calculate_num_gallons(gas_price, num_gal):
    try:
        float(gas_price)
        float(num_gal)
    except:
        return "error in string"
    else:
        return float(gas_price) * float(num_gal)


print(calculate_num_gallons(gas_price, num_gal))

10
9
8
7
6
5
4