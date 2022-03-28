def reverseAdd(num):
    reverse = num[::-1]
    num = str(int(num) + int(reverse))
    if not num == num[::-1]:
        num = reverseAdd(num)
    return num

num = input("enter a num: ")
print(reverseAdd(num))