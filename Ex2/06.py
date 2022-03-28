num = int(input('Enter number of tuples: '))
TupleList = [tuple(map(str, input('Enter Tuple: ').split())) for i in range(num)]
for i in range(num):
    if len(TupleList[i]) == 0:
        del TupleList[i]
print(TupleList)