import re
string = input("Enter string: ")
cleanString = re.sub('\W+','', string )
print(cleanString)