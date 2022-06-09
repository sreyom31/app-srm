# Write a Python program to filter only vowels from given sequence.

def pro_vowel(c):
    newstr = c
    vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
    for x in c:
        if x not in vowels:
            newstr = newstr.replace(x,"")
    return newstr

a=input("Enter string: ")
print(pro_vowel(a))