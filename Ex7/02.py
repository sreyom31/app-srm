# Write a Python program to find the numbers of a given string and store them in a list, display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.

str1 = input()
print("Original string: ",str1)
str_num=[i for i in str1.split(' ')]
length=len(str_num)
numbers=sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
for i in ((filter(lambda x:x>length,numbers))):
    print(i,end=' ')