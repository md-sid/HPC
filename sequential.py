import time
from multiprocessing import Pool

def printifprime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                break
        else:
            print(num)

#sequential
t = time .time()
for number in range(0,100000):
    printifprime(number)
t1 = time.time() - t
