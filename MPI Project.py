import time
import random
import bisect
from time import perf_counter

numbers = list(range(50000, 1, -1))

#with open('arr.txt', 'w') as f:
 #   for number in numbers:
  #   f.write(f"{number} ")

# Sorting algorithms implementations

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Tim Sort implementation (using Python's built-in sorted function as it's based on Tim Sort)
def tim_sort(arr):
    return sorted(arr)


# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# Bogo Sort implementation (not recommended for large lists)
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr


# Bucket Sort implementation
def bucket_sort(arr):
    bucket = []
    slot_num = 10  # 10 means 10 slots, each slot's size is 0.1
    for i in range(slot_num):
        bucket.append([])

    # Put array elements in different buckets
    for j in arr:
        index_b = int(slot_num * j / max(arr))
        if index_b == slot_num:
            index_b -= 1
        bucket[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        bucket[i] = sorted(bucket[i])

    # Concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr


# Utility function to load data from file
def load_data(file_path):
    with open(file_path, 'r') as file:
        # Read the entire file content and replace newlines with spaces
        file_content = file.read().replace('\n', ' ')
        # Split the content into numbers based on spaces
        numbers = file_content.split()
        # Convert each number to an int and return the list
        arr = [int(number) for number in numbers]
    return arr


# Function to measure execution time and memory usage
def measure_performance(sort_function, data):
    start_time = perf_counter()
    sorted_data = sort_function(data)
    end_time = perf_counter()
    time_elapsed = end_time - start_time
    return time_elapsed


# Main function to run experiments
def run_experiments(data_files):
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Quick Sort': quick_sort,
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort,
        'Tim Sort': tim_sort,
        'Merge Sort': merge_sort,
        # 'Bogo Sort': bogo_sort,
        'Bucket Sort': bucket_sort,
    }

    for file_name in data_files:
        data = load_data(file_name)
        print(f"\nResults for {file_name}:")
        for name, function in algorithms.items():
            # Ensure a fresh copy of the data for each sort to ensure fairness
            data_copy = data[:]
            time_elapsed = measure_performance(function, data_copy)
            print(f"{name}: {time_elapsed:.4f} seconds")


data_files = ['arr.txt']
run_experiments(data_files)