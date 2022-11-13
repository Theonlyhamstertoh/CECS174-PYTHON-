user_string = "a asflakjsf"
letter = user_string[0]
phrase = user_string[2:]
count = 0
for char in [*phrase]:
    if char == letter: count += 1

if count > 1:
    print(f"{count} {letter}'s")
elif count > 0:
    print(count, letter)
else:
    print(f"0 {letter}'s")
