# Import required modules 
import time
from multiprocessing import Array, Process, Value
from random import randrange

# Select the size of array to generate and sort
size = 1000
# Select the number of threads to use
nthreads = 40

# One instance of bublesort process 
def bubbleSortPar(arr,i,position,workers):
    n = len(arr)
    # Traverse the array
    for j in range(0, n-1):
        # Set current position
        position[i] = j
        # Check that preceeding thread is far enough ahead
        if i > 0 :
            while position[i-1] < j+3 :
                i=i
        # Swap if the element found is greater than the next element
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
    # Set position to past end of array indicating thread is finished
    f = n+10
    position[i] = f
    workers.value -= 1

# Create empty array in shared memory
arr = Array('i', range(size))

# Initialize array with random numbers
for i in range(size) :
    arr[i]=randrange(500)

# Create empty array in shared memory to track thread locations
position = Array('i', range(size+2))

# Set up thread limiting
maxworkers = nthreads-1
workers = Value('i', 0)
n = 0

t = time.time()  
# Run the algorithm
for i in range (size):
    while workers.value >= maxworkers :
        n = n
    workers.value +=1
    Process(target=bubbleSortPar, args=(arr,i,position,workers)).start()
# Setup and run a final instance to ensure all threads finish before continuing
last = size
p = Process(target=bubbleSortPar, args=(arr,last,position,workers))
p.start()
# Wait for final instance to complete before continuing 
p.join()
# See how long it took
t2 = time.time() - t

# Print sorted array
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 
# Print algorithm runtime
print(t2)
