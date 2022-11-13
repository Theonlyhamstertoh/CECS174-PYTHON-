import math
'''
# Test Cases #
1. Start with 25n, 25d, 25q
2. All coins should be positive
3. Repeatly request user purchase after run or quit
4. all price are factors of 0.05
5. user should not be allowed to purchase if below price
6. Valid Letter
7. Output remaining stock of coins and dollars after
8. Greedy Algo to minimize coin deposit
'''
" "
# INITIALIZE STOCK
stock = {"q": 25, "d": 25, "n": 25, "o": 0, "f": 0}

user_total = 0


# James
def print_stock():
    print("Stock contains: ")
    print(
        f"\t{ stock['q'] } Quarters\n\t{stock['d']} Dimes\n\t{stock['n']} Nickels\n\t{stock['o']} Ones\n\t{stock['f']} Fives"
    )


#Marley
menu_text = (
    "Menu for deposits\n\t'n' - deposit a nickel\n\t'd' - deposit a dime\n\t'q' - deposit a quarter\n\t'o' - deposit a one dollar bill\n\t'f' - deposit a five dollar bill\n\t'c' - cancel the purchase"
)


# The price is already checked and validated
# called when user inputs "c"
def get_change(price):
    # Multiply the price by 100 and convert to int
    # price = round(price * 100)

    # Get all quarters
    quarters = (price // 25)
    price -= quarters * 25
    # Get all dimes
    dimes = (price // 10)
    price -= dimes * 10
    # Get all nickels
    nickels = price // 5
    price -= nickels * 5

    # update stock
    stock['q'] -= quarters
    stock['q'] -= dimes
    stock['n'] -= nickels

    if quarters != 0: print(quarters, 'quarters')
    if dimes != 0: print(dimes, 'dimes')
    if nickels != 0: print(nickels, ' nickels')


def get_payment(price):

    dollars = price // 100
    cents = price - (dollars * 100)
    return f'Payments Due: {dollars} dollars and {cents} cents'

    # return a string: Payment due x dollar(s) and y cents


# Get user input and convert to float if possible, else stay string
def request_purchase_price():
    user_input = (input("Enter the purchase price (xx.xx) or `q' to quit: "))
    try:
        float(user_input)
    except:
        return user_input
    else:
        return round(float(user_input) * 100)


def get_user_deposit():
    user_input = input('Indicate your deposit: ')
    if user_input in stock:
        stock[user_input] += 1
        print_stock()
    if user_input == 'n':
        return 5
    elif user_input == 'd':
        return 10
    elif user_input == 'q':
        return 25
    elif user_input == 'o':
        return 100
    elif user_input == 'f':
        return 500
    else:
        print(f"Illegal selection: {user_input} ")
        return False
        # if user enters illegal,
        # rerun the function


def start_vending_machine():
    print('Welcome to the vending machine change maker program')
    print('Change maker initialized.')
    print_stock()

    while True:
        price = request_purchase_price()

        # check if price is illegal
        if (price == "q"):
            print("EXIT, BREAK!")
            break
        elif price < 0 or price % 5 != 0:
            print(
                'Illegal price: Must be a non-negative multiple of 5 cents. ')
            continue
        else:
            # PRICE IS VALIDATED HERE
            print(menu_text)
            while True:

                # output payment user is due
                print(get_payment(price))
                deposit = get_user_deposit()
                if deposit == False: continue

                # we get the deposit and subtract from the total price
                price -= deposit

                if price <= 0:
                    print("ALL PAID AND RETURN CHANGE")
                    print(get_change(abs(price)))
                    break
                continue


start_vending_machine()
