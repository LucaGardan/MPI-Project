import time
import random
import bisect
from time import perf_counter

numbers = list(range(50001))

last_500 = numbers[-500:]
random.shuffle(last_500)
numbers[-500:] = last_500

corrected_nearly_sorted_flat_list_string = ' '.join(map(str, numbers))

file_path_flat='arr.txt'

with open(file_path_flat, 'w') as file:
    file.write(corrected_nearly_sorted_flat_list_string)

file_path_flat
