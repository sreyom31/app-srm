from threading import *
from time import sleep

item_list = []
lock = Lock()

def producer():
    lock.acquire()
    for i in range(10):
        item_list.append(i)
        print("Item Produced: ", i)
        lock.release()
        sleep(2)
        lock.acquire()
    lock.release()

def consumer():
    lock.acquire()
    while item_list:
        print("Item consumed", item_list[0])
        item_list.pop(0)
        lock.release()
        sleep(5)
        lock.acquire()    
    lock.release()

T1 = Thread(target = producer)
T2 = Thread(target = consumer)
T1.start()
T2.start()
T1.join()
T2.join()
