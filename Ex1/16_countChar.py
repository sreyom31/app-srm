counter = {chr(val): 0 for val in range(97, 124)}

str1 = input("enter the string: ")

for char in str1:
    if not char == " ":
        counter[char] += 1

for char in str1:
    if not char == " ":
        print(char, counter[char], end=",")