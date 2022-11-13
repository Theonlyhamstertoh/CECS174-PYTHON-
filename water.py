import math

code = str.lower(input("Enter the customer\'s code: "))
gallons_beginning = float(
    input("Enter the customer\'s beginning meter reading: "))
gallons_end = float(input("The customer\'s ending meter reading: "))
if gallons_beginning > gallons_end:
    gallons_used = ((1000000000 + gallons_end) - gallons_beginning) * 0.1
else:
    gallons_used = (math.fabs(gallons_end - gallons_beginning)) * 0.1

if code == "r":
    gallons_cost = 5.00 + (0.0005 * gallons_used)
elif code == "c":
    if gallons_used <= 4000000:
        gallons_cost = 1000.00
    else:
        gallons_cost = 1000.00 + (0.00025 * (gallons_used - 4000000))
elif code == "i":
    if gallons_used <= 4000000:
        gallons_cost = 1000.00
    elif 4000000 < gallons_used <= 10000000:
        gallons_cost = 2000.00
    else:
        gallons_cost = 2000.00 + (0.00025 * (gallons_used - 10000000))
else:
    gallons_cost = 0.00
    gallons_used = 0.0

print(f"Customer code: {code}")
print(f"Beginning meter reading: {gallons_beginning:09.0f}")
print(f"Ending meter reading: {gallons_end:09.0f}")
if gallons_cost == 0.00:
    print("Invalid entry")
    print(f"Gallons of water used: {gallons_used:.1f}")
else:
    print(f"Gallons of water used: {gallons_used:.1f}")
print(f"Amount billed: ${gallons_cost:.2f}")