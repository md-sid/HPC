import sys

def printifprime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                break
        else:
            print(num)

input = int(sys.argv[1])+1000000
printifprime(input)
