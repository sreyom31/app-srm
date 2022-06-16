from _thread import *
from threading import Thread


def printFromThread(num):
    print("Hello From Thread: ", num)


threadArr = []
for i in range(50):
    threadArr.append(Thread(target=printFromThread, args=[i+1]))

for i in reversed(threadArr):
    i.start()