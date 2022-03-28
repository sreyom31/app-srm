num = ''
for i in range(10):
    num = str(i)
    for j in range(10):
        num += str(j)
        for k in range(10):
            num += str(k)
            print(num)
            num = str(i) + str(j)
        num = str(i)