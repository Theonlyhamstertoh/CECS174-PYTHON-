tax_income = float(input("What is your 2019 taxable income? "))
current_bracket = {
    "wealthy": .32 * (tax_income - 160725),
    "high": .24 * (tax_income - 84200),
    "mid": .22 * (tax_income - 39475),
    "low": .12 * (tax_income - 9700),
    "bottom": .10 * (tax_income - 0),
}

marginal_brackets = {
    "wealthy": .32 * (204100 - 160725),
    "high": .24 * (160725 - 84200),
    "mid": .22 * (84200 - 39475),
    "low": .12 * (39475 - 9700),
    "bottom": .10 * (9700 - 0),
}

def addAllBrackets(current, brackets):
    total = current_bracket[current]
    if len(brackets) == 0: return total

    for bracket_type in brackets:
        total += marginal_brackets[bracket_type]
    return total


def findTax(income):
    # find current bracket tax
    if income in range(160725, 204100):
        return addAllBrackets("wealthy", ["bottom", "low", "mid", "high"])
    if income in range(84200, 160725):
        return addAllBrackets("high", ["bottom", "low", "mid"])

    if income in range(39475, 84200):
        return addAllBrackets("mid", ["bottom", "low"])
    if income in range(9700, 39475):
        return addAllBrackets("low", ["bottom"])
    if income in range(0, 9700):
        return addAllBrackets("bottom", [])


total_tax = findTax(tax_income)
print(f"Your tax liability is ${total_tax:,.2f}")
print(f"Your effective tax rate is {total_tax / tax_income* 100:,.1f}%")
