import math

magnitude_scale = float(input("Please enter a Richter Scale Value: "))
energy = math.pow(10, (1.5 * magnitude_scale) + 4.8)
oneTonOfTNT = 4.184e9
exploded_tnt_ton = energy / oneTonOfTNT

# pre-generated scales
print("{:<10} {:<32} {}".format('Richter', "Joules", "TNT"))

# [ 1 ] Richter Scale
ONE = 1
energy2 = math.pow(10, (1.5 * ONE) + 4.8)
exploded_tnt_ton2 = energy2 / oneTonOfTNT
print("{:<10} {:<32} {:<20}".format(ONE, energy2, exploded_tnt_ton2))

# [ 5 ] Richter Scale
FIVE = 5
energy2 = math.pow(10, (1.5 * FIVE) + 4.8)
exploded_tnt_ton2 = energy2 / oneTonOfTNT
print("{:<10} {:<30} {:<20}".format(FIVE, energy2, exploded_tnt_ton2))

# [ 9.1 ] Richter Scale
NINE_ONE = 9.1
energy2 = math.pow(10, (1.5 * NINE_ONE) + 4.8)
exploded_tnt_ton2 = energy2 / oneTonOfTNT
print("{:<10} {:<24} {:<20}".format(NINE_ONE, energy2, exploded_tnt_ton2))

# [ 9.2 ] Richter Scale
NINE_TWO = 9.2
energy2 = math.pow(10, (1.5 * NINE_TWO) + 4.8)
exploded_tnt_ton2 = energy2 / oneTonOfTNT
print("{:<10} {:<24} {:<20}".format(NINE_TWO, energy2, exploded_tnt_ton2))

# [ 9.5 ] Richter Scale
NINE_FIVE = 9.5
energy2 = math.pow(10, (1.5 * NINE_FIVE) + 4.8)
exploded_tnt_ton2 = energy2 / oneTonOfTNT
print("{:<10} {:<23} {:<20}".format(NINE_FIVE, energy2, exploded_tnt_ton2))

# User input magnitude scale
print(f"Richter Scale Value: {magnitude_scale}")
print(f"Equivalence in Joules: ", energy)
print(f"Equivalence in tons of TNT: ", exploded_tnt_ton)
