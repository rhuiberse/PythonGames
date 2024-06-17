


def deposit():
    while True:
        amount = input('What is the amount you want to deposit? €')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: print('Amount must be greater that 0')
        else:
            print('Please enter a number')

    return amount


deposit()
                