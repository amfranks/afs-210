import time
import random

def quicksort_last(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point.
    pivot = partitionStart(a_list, start, end)
    quicksort_last(a_list, start, pivot-1)
    quicksort_last(a_list, pivot+1, end)
        

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

def partition(a_list, start, end):

    # Select the last index as our pivot point 
    pivot = a_list[end]
    pivotIndex = start

    for i in range(start, len(a_list)):
        if a_list[i] < pivot:
            a_list[i], a_list[pivotIndex] = a_list[pivotIndex], a_list[i]
            pivotIndex += 1
    a_list[pivotIndex], a_list[end] = a_list[end], a_list[pivotIndex]

    return pivotIndex
            
####################################################################

print("Quick Sort:")
myList = [x for x in range(1000)]
random.shuffle(myList)

start_time = time.time()
quicksort_last(myList, 0, len(myList) - 1)
# quicksort_random(myList, 0, len(myList) - 1)
end_time = time.time()
print("Sorted Listed: ")
print(myList)   

print(f"The execution time is: {end_time-start_time}")