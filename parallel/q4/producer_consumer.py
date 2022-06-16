from threading import *
from time import sleep 

limit = int(input("Enter Limit For Producer Arr: "))
items = []
items_cv = Condition()

def producer():
    for i in range(30):
        with items_cv:
            while len(items) > limit:
                items_cv.wait()
            print('Item Produced: ', i)
            items.append(i)
            items_cv.notify()
        sleep(1)

def consumer():
    while True:
        with items_cv:
            while not items:
                items_cv.wait()
            x = items.pop(0)
            items_cv.notify()
        print("Item consumed: ", x)
        sleep(5)

T = Thread(target=consumer)
T.setDaemon(True)
T.start()

producer()