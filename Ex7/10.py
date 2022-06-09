# Filter the array, and return a new array with only the values equal to or above 18 ( consider filter function)

def pro_vowel(c):
    newstr = c
    vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
    for x in c:
        if x not in vowels:
            newstr = newstr.replace(x,"")
    return newstr

a=input("Enter string: ")
print(pro_vowel(a))