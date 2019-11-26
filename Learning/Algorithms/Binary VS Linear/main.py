"""
Complete the provided spreadsheet by changing the values in this program
according to the spreadsheet and record the results.
"""


import timeit
from typing import List

def linear_search(target: int, data: List) -> int:
    for i, num in enumerate(data):
        if num == target:
            return i
    
    return -1


def binary_search(target: int, data: List) -> int:
    start = 0
    end = len(data) -1
    mid = (start + end) // 2

    while True:
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid
            mid = (start + end) // 2
        elif data[mid] < target:
            start = mid
            mid = (start + end) // 2
        
        if end - start == 1:
            return -1


for i in range(1, 12):
    DATASET_SIZE = 10**i
    NUMBER = 1
    SEARCH_TARGET = DATASET_SIZE - 1
    
    # dataset = list(range(DATASET_SIZE))
    dataset = (range(DATASET_SIZE))

    result = timeit.timeit(
        "linear_search(SEARCH_TARGET, dataset)",
        number=NUMBER,
        globals=globals())

    print(result)