num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
if num1 == num2:
    print(True)
elif abs(int(num1)-int(num2)) == 5 or int(num1)+int(num2) == 5:
    print(True)
else:
    print(False)