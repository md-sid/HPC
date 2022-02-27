# Import required modules 
import time
from random import randrange

# Select size of array to generate and sort
size = 1000

# The simple bublesort algorithm 
def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through array as many times as there are array elements 
    for i in range(n):
  
        # Traverse the array from 0 to n-1
        for j in range(0, n-1):
  
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
# Create an array of desired size
arr = [0] * size
# Initialize array with random numbers
for i in range(size) :
    arr[i]=randrange(500)

t = time.time()
# Run the algorithm 
bubbleSort(arr)
# Calculate how long it took
t2 = time.time() - t

# Print out the sorted array
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 
# Print algorithm runtime
print(t2)
