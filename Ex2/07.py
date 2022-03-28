count = 0
TupleList = [4 , (), 'd', 8, (4, 6, 7)]
for i in range(len(TupleList)):
    if type(TupleList[i]) is tuple:
        break
    count += 1

print(count)