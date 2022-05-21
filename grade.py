# variables containing the grades for the input and the letter grade
aplus = 98
aminus = 95
a = 92
bplus = 88
bminus = 85
b =  82
cplus =78 
cminus = 75
c = 72 
# Ask what score you got in class
print('What Score Did you Get? ')
x = int(input())
# check to see if the input matches the variable and if it matches display the letter grade
if x == 98: 
    print('A +')
elif x == 95:
    print('A -')
elif x == 92:
    print('A')
elif x == 88:
    print('B +')
elif x == 85:
    print('B -')
elif x == 82:
    print(' B')
elif x == 78:
    print('C +')
elif x == 95:
    print(' C -')
elif x == 95:
    print('C')
else:
    print(' You Going To Have To Redo This Class')