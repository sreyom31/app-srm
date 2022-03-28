string = input("enter string: ")
def reverse(string):
    return string[::-1]
def check_palindrome(string):
    return string == reverse(string)
print(check_palindrome(string))