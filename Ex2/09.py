c = 0
arr = [8,7,3,2,1,8,18,9,7,3,4]
for i in range(len(arr)):
    if arr.count(i) == 1:
        c += 1
print(c) 
