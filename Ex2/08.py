myList = [[(8,3), (5,6)], [(7,8), (11,13)]]
converted = [elt for sub in myList for elt in sub]
print(converted)
res = list(zip(*converted))
print(res)