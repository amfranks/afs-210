import time
import random

# def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    # if start >= end:
        # return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    # pivot = partitionStart(a_list, start, end)
    # quick_sort(a_list, start, pivot-1)
    # quick_sort(a_list, pivot+1, end)
        

# def partitionStart(a_list, start, end):
#     return partition(a_list, start, end)

# def partition(a_list, start, end):

#     # Select the first element as our pivot point 
#     pivot = a_list[start]
    
#     # Start at the first element past the pivot point
#     low = start + 1
#     high = end

#     while True:
#         # If the current value we're looking at is larger than the pivot
#         # it's in the right place (right side of pivot) and we can move left,
#         # to the next element.
#         # We also need to make sure we haven't surpassed the low pointer, since that
#         # indicates we have already moved all the elements to their correct side of the pivot
#         while low <= high and a_list[high] >= pivot:
#             high = high - 1

#         # Opposite process of the one above
#         while low <= high and a_list[low] <= pivot:
#             low = low + 1

#         # We either found a value for both high and low that is out of order
#         # or low is higher than high, in which case we exit the loop
#         if low <= high:
#             # Swap the values
#             a_list[low], a_list[high] = a_list[high], a_list[low]
#             # The loop continues
#         else:
#             # We exit out of the loop
#             break

#     # Swap the values
#     a_list[start], a_list[high] = a_list[high], a_list[start]

#     return high

    #############################################################################################

    # Select the last index as our pivot point 
    # pivot = a_list[end]
    # pivotIndex = start

    # for i in range(start, len(a_list)):
    #     if a_list[i] < pivot:
    #         a_list[i], a_list[pivotIndex] = a_list[pivotIndex], a_list[i]
    #         pivotIndex += 1
    # a_list[pivotIndex], a_list[end] = a_list[end], a_list[pivotIndex]

    # return pivotIndex
            
    #############################################################################################


def quicksort_random(a_list, start , end):
    if(start < end):
          
        # pivotindex is the index where the pivot lies in the array.
        pivotindex = partitionrand(a_list, start, end)
          
        # At this stage the array is 
        # partially sorted around the pivot. 
        # Separately sorting the 
        # left half of the array and the
        # right half of the array.
        quicksort_random(a_list , start , pivotindex-1)
        quicksort_random(a_list, pivotindex + 1, end)
  
# This function generates random pivot,
# swaps the first element with the pivot 
# and calls the partition function.
def partitionrand(a_list , start, end):
  
    # Generating a random number between the 
    # starting index of the array and the
    # ending index of the array.
    randpivot = random.randrange(start, end)
  
    # Swapping the starting element of
    # the array and the pivot
    a_list[start], a_list[randpivot] = \
        a_list[randpivot], a_list[start]
    return partition(a_list, start, end)
  
'''
This function takes the first element as pivot, 
places the pivot element at the correct position 
in the sorted array. All the elements are re-arranged 
according to the pivot, the elements smaller than the
pivot is places on the left and the elements
greater than the pivot is placed to the right of pivot.
'''

def partition(a_list, start, end):
    pivot = start # pivot
      
    # a variable to memorize where the 
    i = start + 1 
      
    # partition in the array starts from.
    for j in range(start + 1, end + 1):
          
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if a_list[j] <= a_list[pivot]:
            a_list[i] , a_list[j] = a_list[j] , a_list[i]
            i = i + 1
    a_list[pivot] , a_list[i - 1] = a_list[i - 1] , a_list[pivot]
    pivot = i - 1
    return (pivot)
    



print("Quick Sort:")
myList = [x for x in range(1000)]
random.shuffle(myList)

start_time = time.time()
# quick_sort(myList, 0, len(myList) - 1)
quicksort_random(myList, 0, len(myList) - 1)
end_time = time.time()
print("Sorted Listed: ")
# print(myList)   

print(f"The execution time is: {end_time-start_time}")