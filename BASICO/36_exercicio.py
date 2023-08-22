"""
Iterando strings com while
"""
#       012345678910
string = 'Adalberto Bengaly'  # Iteráveis
#      1110987654321

i = 0
newString = ''
while i < len(string):
    newString += "*" + string[i] 
    i += 1

newString += "*"
print(newString)