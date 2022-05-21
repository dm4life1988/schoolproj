# dictionary lists can be unordered and they are indexed through their keys which referes to their key value pairs
dict = {11 : 'a', 22 : 'b', 33 : 'c'} # i used integers as my key then strings as my key value pairs
dict2 = {33 : 'c', 22 : 'b', 11 : 'a'} # this is the same dictionary just backwards to show that they can be un ordered and still show True
print(dict[11]) # Shows how to call the dictionary key value pair by the Key
print(dict[22]) # just another example
print(dict == dict2) # showing that the dictionarys show True being that they are un ordered but the Keys and Key value pairs are the same 
dict2[44] = 'd' # I added a new Key named 44 with a key value of 'd' 
print(dict == dict2) # now dict2 is different because I added a new pair so it is False
print(dict2)



