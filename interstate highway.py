# primary = 1/2 digits,
#   odd - NS
#   even - EW
#   size - 5x are long-distance
# aux route: 3 digits
#    odd - Spur
#     even - loop highway
#   two last digit is the parent highway


def checkIfPrimaryHighway(highway_num):
    orientation = "north-south"
    # primary route
    if int(highway_num) % 2 == 0:
        orientation = "east-west"
    if int(highway_num) % 5 == 0:
        print(
            f"Interstate {highway_num} is a long-distance arterial highway oriented {orientation}."
        )
        return
    print(f"Interstate {highway_num} is oriented {orientation}.")


def checkIfAuxHighway(highway_num):
    parent_highway = user_input[1:]
    highway_type = "spur"

    if int(highway_num[0]) % 2 == 0:
        highway_type = "loop"
    print(
        f"Interstate {highway_num} is a {highway_type} highway of Interstate {int(parent_highway)}."
    )


while True:
    user_input = (input("Please enter a US Interstate Highway route number: "))
    try:
        int(user_input)
    except:
        continue

    if int(user_input) == 0:
        break

    if 0 <= int(user_input) <= 999:
        if len(user_input) == 2 or len(user_input) == 1:
            checkIfPrimaryHighway((user_input))
        elif len(user_input) == 3:
            checkIfAuxHighway((user_input))

# int param
