from cgitb import small


password = input("Enter a password: ")
symbols = ['$', '#', '@']
small_letters = [chr(char) for char in range(65, 92)]
capital_letters = [chr(char) for char in range(97, 124)]
numbers = [str(num) for num in range(10)]
isSymbol = False
isSmall = False
isCapital = False
isNum = False

if len(password) > 16 or len(password) < 6:
    pass
else:
    for char in password:
        if char in symbols:
            isSymbol = True
        elif char in small_letters:
            isSmall = True
        elif char in capital_letters:
            isCapital = True
        elif char in numbers:
            isNum = True

if isSymbol and isSmall and isCapital and isNum:
    print("valid password")
else:
    print('Not a valid password')