def subSum(n):
    s=0
    for i in str(n):
        s += int(i)
    if (n-s > 0):
        print(n-s)
        subSum(n-s)

num = int(input("Enter number: "))
if num>0:
    subSum(num)