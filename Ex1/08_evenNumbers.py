for num in range(100, 401):
    toPrint = True
    for i in str(num):
        if (int(i) % 2):
            toPrint = False
    if toPrint:
        print(num, end=", ")