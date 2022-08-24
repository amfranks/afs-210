import time
import random

mediancomparison = 0

def quicksort_median(array, leftindex, rightindex):
     global mediancomparison
     
     if leftindex < rightindex:
         newpivotindex = partition_median(array, leftindex, rightindex)
         mediancomparison += (rightindex - leftindex - 1)

         quicksort_median(array, leftindex, newpivotindex)
         quicksort_median(array, newpivotindex + 1, rightindex)

# Calculate the median of three numbers using two comparisons.
def median(a, b, c):
    if (a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c

# Partition around the median
def partition_median(a_list, start, end):
    left = a_list[start]
    right = a_list[end-1]
    length = end - start
    if length % 2 == 0:
        middle = a_list[start + length // 2 - 1]
    else:
        middle = a_list[start + length // 2]
  
    

    pivot = median(left, right, middle)

    pivotindex = a_list.index(pivot) # All values in array must be unique.

    a_list[pivotindex] = a_list[start]
    a_list[start] = pivot

    i = start + 1
    for j in range(start + 1, end):
        if a_list[j] < pivot:
            temp = a_list[j]
            a_list[j] = a_list[i]
            a_list[i] = temp
            i += 1

    startval = a_list[start]
    a_list[start] = a_list[i-1]
    a_list[i-1] = startval
    return i - 1 

####################################################################

print("Quick Sort:")
myList = [x for x in range(1000)]
random.shuffle(myList)

start_time = time.time()
quicksort_median(myList, 0, len(myList) - 1)
end_time = time.time()
print("Sorted Listed: ")
print(myList)   

print(f"The execution time is: {end_time-start_time}")