# Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.

def change_cases(s):
  return str(s).upper(), str(s).lower()
 
chrars = input("Enter string: ")
result = map(change_cases, chrars)
print("\nAfter eliminating duplicate letters:")
print(set(result))