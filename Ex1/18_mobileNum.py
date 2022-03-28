userNum = input("enter mobile num: ")
numbers = [str(i) for i in range(10)]

for num in userNum:
    if num in numbers:
        numbers.remove(num)

for i in numbers:
    print(i)