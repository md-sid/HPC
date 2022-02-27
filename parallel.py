import time
from multiprocessing import Pool

def printifprime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                break
        else:
            print(num)

#parallel
t = time.time()
with Pool(40) as p:
	p.map(printifprime, range(0,100000))
t2 = time.time() - t
print(t)
print(t2)
