# Binary Search
from typing import List
from os import system

# List must be:
# - Sorted (Least to greatest)
# - Have no repeats
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


# test stuff

def test_empty_list():
    assert binary_search(5, []) == -1


def test_number_not_found():
    dataset = list(range(100))
    assert binary_search(100, dataset) == -1

    dataset = list(range(3))
    assert binary_search(100, dataset) == -1


def test_found_last_index():
    dataset = list(range(100))
    assert binary_search(99, dataset) == 99


def test_found_middle_index():
    dataset = list(range(3))
    assert binary_search(1, dataset) == 1

    dataset = list(range(100, 200))
    assert binary_search(134, dataset) == 34


def test_found_first_index():
    dataset = list(range(100))
    assert binary_search(0, dataset) == 0