def divideby(number):

    return int(number) / 10

while True:
    divideby10 = input('Input a number, or type "quit" to quit: ')
    if divideby10 == 'quit' or divideby == '"quit" ':
        break
    result = divideby(divideby10)
    print(f"10 divided by your number is {result}!")