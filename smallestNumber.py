# SMALLEST NUMBER
print(min([int(input()), int(input()), int(input())]))

# CAFFEINE
amount = float(input())
hour6 = amount / 2
hour12 = amount / 4
hour24 = amount / 16
print(f'After 6 hours: {hour6:.2f}mg')
print(f'After 12 hours: {hour12:.2f}mg')
print(f'After 24 hours: {hour24:.2f}mg')

par = int(input())
score = int(input())

if par == score:
    print("Par")
elif par == score - 1:
    print('Bogey')
elif par == score + 1:
    print('Birdie')
elif par == score + 2:
    print('Eagle')
