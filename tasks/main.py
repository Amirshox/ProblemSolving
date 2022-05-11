import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))


for i in range(5):
    worker(i)

print("All Threads are queued, let's see when they finish!")

