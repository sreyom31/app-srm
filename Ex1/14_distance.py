import math
str1 = list(map(int, input("enter 1st coordinates: ").split()))
str2 = list(map(int, input("enter 1st coordinates: ").split()))

print(math.sqrt((str2[1]-str1[1]) ** 2 + (str2[0] - str1[0]) ** 2))