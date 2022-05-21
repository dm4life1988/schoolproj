acronym_dict = {
    'A': 'Address', 'AD': 'Active Directory', 


}

def network(acronym):
    try:
        if acronym_dict[acronym] == acronym_dict[acronym]:
            return acronym_dict[acronym] 
    except KeyError:
        return 'Is Not in the system'
test = network('A')
print(test)