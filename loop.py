accountBalance = int(input('Please enter the balance.'))

if accountBalance == 0:
    print('Ouch. I remember being a broke student, too.')
elif accountBalance < 1000:
    print('Penny-pinching makes a difference.')
elif accountBalance  <= 1000:
    print('Nice, you are paying for lunch!')
elif accountBalance <= 100000:
    print('Can I have some investment tips?')
elif accountBalance <= 1000000000:
    print('Nice job Photoshopping your balance statement.')