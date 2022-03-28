n = int(input('Enter number of tuples: '))
m = int(input('Enter no of elements in a tuple: '))
mytupleArr = [tuple(map(int, input('Enter elts of first tuple').split())) for i in range(n)]
sumedTuple = []
for i in range(m):
    sum = 0
    for j in range(n):
        sum += mytupleArr[j][i]
    sumedTuple.append(sum)
sumedTuple = tuple(sumedTuple)     
print(sumedTuple)