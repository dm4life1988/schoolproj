ports = {
        "53": "DNS",
        "80": "HTTP",
        "443": "HTTPS",
}


def protocol(input):
        try:
                if ports[input] == ports[input]:
                        return ports[input]
                else:
                        return "invalid"
        except (ValueError, KeyError):
                return "Invalid input"
        
user_input = input("What port would you like to check?: ")
test = protocol(user_input)
print(test)
def basic(x):
        x = user_input1
        if x < 1023:
                print('Well Known Port')
        elif x <= 49151:
                print('Registered Port')
        elif x <= 65535:
                 print('Dynamic ')
        else:
            print('Not a Port Number')
            
user_input1 = int(input('What Port Range?: '))
test1 = basic(user_input1)
print(test1)

