# m1 = float(input())
# m2 = float(input())


# validate value is positive and loop if not
# find which earthquake had the higher mag
# calculate relative mag
def get_magnitude(number):

    try:
        mag_scale = float(
            input(f"Please enter the magnitude for earthquake {number}: "))
        if mag_scale < 0:
            return get_magnitude(number)
        else:
            print('what')
            return mag_scale
    except:
        return get_magnitude(number)


def compare_magnitudes(mag1, mag2):
    return (10**(1.5 * ((mag1 - mag2))))


def get_run_again():
    try:
        num = (input("Try again? Type 1 for yes: "))
        if int(num) == 1:
            return True
        return False
    except:
        return False


# print(get_run_again())

while True:
    mag1 = get_magnitude(1)
    print(mag1)
    mag2 = get_magnitude(2)
    mag_diff = compare_magnitudes((mag1), (mag2))

    print(
        f"An earthquake of magnitude {mag1 if mag1 > mag2 else mag2 } is {mag_diff if mag1 > mag2 else 1/mag_diff:.1f} times more powerful than an earthquake of magnitude {mag2 if mag1 > mag2 else mag1 }. "
    )

    if get_run_again():
        continue
    else:
        print('Bye!')
        break
# print(compare_magnitudes(9.1, 7.1))
# def get_run_again():
