# task_1
def partition(arr, low, high):
    pivot = arr[high] # choosing the last element as the pivot
    i = low - 1 # pointer for smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 # increment the index i

            arr[i], arr[j] = arr[j], arr[i] # swap the elments to place greter element to right side
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # placing the pivot in correct position
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1) # recursively sort left side
        quick_sort(arr, partition_index + 1, high) # sort the right side

test = [23, 34, 67, 87, 12, 70, 40]
low, high = 0, len(test) - 1
quick_sort(test, low, high)
print("sorted array:", test)

# task_1
def bubble_sort(arr):
    length = len(arr)

    for i in range(length): # iterate through each element
        swapped = False # If not swapped 
        for j in range(0, length - i - 1):
            # compare the current element with the next element
            if arr[j] > arr[j + 1]:
                # swap the element if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True # set swapped to Trun to show swap occured
        if not swapped: # if no swap are made, it means array is sorted
            # get out of the loop
            break
    
    return arr # return the aorted array

test = [46, 29, 20, 42, 30, 40 , 44, 39]
sorted_arr = bubble_sort(test.copy())
print("bubble sort array:", sorted_arr)

# task_3
def insertion_sort(arr, left, right):
    # sort a subarray using insertion sort
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_merge_sort(arr, threshold=10):
    # hybrid merge sort
    if len(arr) <= threshold:
        insertion_sort(arr, 0, len(arr) - 1)
        return arr

    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)

    return merge(left, right)

def merge(left, right):
    merge = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
    merge.extend(left[i:])
    merge.extend(right[j:])
    return merge

test_array = [64, 23, 45, 20, 93, 38, 10, 48, 84]
shorted_array = hybrid_merge_sort(test_array)
print("hybrid merge sort:", shorted_array)

# task_4
import matplotlib.pyplot as plt
import time

# Bubble Sort Algorithm
def bubble_sort(arr, draw, delay):
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                draw(arr)
                time.sleep(delay)
        if not swapped:
            break
    return arr

# Insertion Sort (used in Hybrid Merge Sort)
def insertion_sort(arr, left, right, draw, delay):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            draw(arr)
            time.sleep(delay)
        arr[j + 1] = key

# Hybrid Merge Sort Algorithm
def hybrid_merge_sort(arr, draw, delay, threshold=10):
    if len(arr) <= threshold:
        insertion_sort(arr, 0, len(arr) - 1, draw, delay)
        return arr

    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid], draw, delay, threshold)
    right = hybrid_merge_sort(arr[mid:], draw, delay, threshold)

    return merge(left, right, arr, draw, delay)

# Merge function for Hybrid Merge Sort
def merge(left, right, arr, draw, delay):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        draw(arr)
        time.sleep(delay)

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        draw(arr)
        time.sleep(delay)

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        draw(arr)
        time.sleep(delay)
    return arr

# Visualization function
def visualize_sorting_algorithm(arr, sort_algorithm, delay=0.1):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_title(sort_algorithm.__name__)
    
    def draw(data):
        for rect, val in zip(bar_rects, data):
            rect.set_height(val)
        plt.pause(delay)
    
    sorted_arr = sort_algorithm(arr, draw, delay)
    draw(sorted_arr)
    plt.show()

# Testing with sample array and sorting algorithms
test_array = [46, 29, 20, 42, 30, 40, 44, 39]

print("Visualizing Bubble Sort:")
visualize_sorting_algorithm(test_array.copy(), bubble_sort, delay=0.1)

print("Visualizing Hybrid Merge Sort:")
visualize_sorting_algorithm(test_array.copy(), hybrid_merge_sort, delay=0.1)
