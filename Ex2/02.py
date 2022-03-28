string1 = input("Enter String: ")
string2 = input("Enter String 2: ")

rotationalyEqui = False
count = len(string2)

while count:
    count -= 1
    if(string1 == string2):
        rotationalyEqui = True
        break
    
    string2 = string2[1::] + string2[:1:]


print(rotationalyEqui)