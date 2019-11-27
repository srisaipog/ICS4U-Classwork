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


def binary_search(find: int, numbers: List[int]) -> int:
    first = 0
    last = len(numbers) - 1
    mid = last + first // 2

    while True:

        not_found = (last - first) <= 0

        if not_found:
            return -1
        
        if numbers[mid] == find:
            return mid
        elif numbers[mid] > find:
            last = mid
            mid = (last + first) // 2
        elif numbers[mid] < find:
            first = mid
            mid = (last + first) // 2


for i in range(1, 12):
    DATASET_SIZE = 10**i
    NUMBER = 10
    SEARCH_TARGET = DATASET_SIZE - 1
    # SEARCH_TARGET = 0
    # SEARCH_TARGET = DATASET_SIZE // 2

    # dataset = list(range(DATASET_SIZE))
    dataset = list(range(DATASET_SIZE))

    result = timeit.timeit(
        "binary_search(SEARCH_TARGET, dataset)",
        number=NUMBER,
        globals=globals())

    print(result)