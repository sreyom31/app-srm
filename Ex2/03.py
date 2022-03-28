import random
n = int(input("Enter length of binary number: "))
binaryNum = ''
while n:
    n-=1
    binaryNum += random.choice(['0', '1'])
    
print(binaryNum)