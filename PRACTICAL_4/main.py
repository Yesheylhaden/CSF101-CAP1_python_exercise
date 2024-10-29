import time
import math

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 5

def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i) # add to the indices array
    if not indices:
        return "not found"
    return indices  # Return -1 if the target is not in the list

# Test the function
result = linear_search(test_list, 5)
print(f"Linear Search: Index of {target} is {result}")

# binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # return -1 if the target is not in the list

# test_list = [9, 3, 6, 7, 2, 8]
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, target)
print(f"Binary Search: Index of {target} in sorted list is {result}")

# jump search algorithm
def jump_search( arr, target, n ):
     
    # Finding block size to be jumped
    step = math.sqrt(n)
     
    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while arr[int(min(step, n)-1)] < target:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
     
    # Doing a linear search for target in 
    # block beginning with prev.
    while arr[int(prev)] < target:
        prev += 1
         
        # If we reached next block or end 
        # of array, element is not present.
        if prev == min(step, n):
            return -1
     
    # If element is found
    if arr[int(prev)] == target:
        return prev
     
    return -1
 
# Driver code to test function
n = len(test_list)

# Find the index of 'target' using Jump Search
index = jump_search(test_list_sorted, target, n)
 
# Print the index where 'target' is located
print("Number" , target, "is at index" ,"%.0f"%index)

# comparing search algorithm
def compare_search_algorithms(arr, target):
    # linear search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time

    # binary search 
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start_time

    # jump search 
    arr_sorted = sorted(arr)
    start_time = time.time()
    jump_search_result = jump_search(arr_sorted, target, n)
    jump_search_time = time.time() - start_time

    # printing result
    print(f"linear search: indices of {target} are {linear_result}, time: {linear_time:.6f} seconds")
    print(f"binary search: index of {target} in sorted list is {binary_result}, time: {binary_time} seconds")
    print(f"jump search: index of {target} in sorted list is {jump_search_result} time: {jump_search_time} seconds")

compare_search_algorithms(test_list, target)