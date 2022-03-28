def check(arr):
    for num in arr:
        if num in arr[arr.index(num)+1:]:
            return False
        return True

numbers = list(map(int, input("Enter the numbers: ").split()))

if (check(numbers)):
    print("Different")
else:
    print("Not Different")