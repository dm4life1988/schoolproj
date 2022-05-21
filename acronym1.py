acronym_dict = {
    'A': 'Address', 'AD': 'Active Directory', 


}

def network(acronym):
    try:
        if acronym_dict[acronym] == acronym_dict[acronym]:
            return acronym_dict[acronym] 
    except KeyError:
        return 'Is Not in the system'
    else:
        print('Enter an acronym: (blank to quit)')
        dict2 = input()
        if dict2 == '':
            break
    if dict2 in acronym_dict:
        print(acronym_dict[dict2] + ' is the definition of ' + dict2)
    else:
        print('What is the definition for the acronym?')
        x = input()
        acronym_dict[dict] = x 
        print
test = network('A')
print(test)