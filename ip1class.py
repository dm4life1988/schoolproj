def address_class(address):
    try:
        address = address.split('.')
        oct1 = int(address[0])
        oct2 = int(address[1])
        oct3 = int(address[2])
        oct4 = int(address[3])

        if oct2 < 256 and oct3 < 256 and oct4 < 256:
            if oct1 < 128:
                return 'Class A IP Address'
            elif oct1 < 192:
                return 'Class B IP Address'
            elif oct1 < 224:
                return 'Class C IP Address'
            elif oct1 < 240:
                return 'Class D IP Address'
            elif oct1 < 256:
                return 'Class E IP Address'
            else:
                return 'Invalid IP Address'
        else:
            return 'Invalid IP Address'
    except ValueError:
        return 'Invalid Input'

address = input('What IPv4 Address?: ')
test_ip = address_class(address)
print(test_ip)