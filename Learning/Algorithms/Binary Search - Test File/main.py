"""
Create a function with the following details:
binary_search(target: int, numbers: int) -> int

It will return the index location, not the found value. 
Return -1 if the value is not in the list.
"""

import os
from typing import List

def main():
    pass

'''
def binary_search(target, data):
    first = 0
    last = len(data) - 1
    mid = (first + last) // 2

    while True:
        if (last - first) <= 0:
            return -1
        
        if data[mid] == target:
            return mid
        
        elif data[mid] < target:
            start = mid
            mid = (start + last) // 2
        
        elif data[mid] > target:
            last = mid
            mid = (start + last) // 2
'''


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


if __name__ == "__main__":
    os.system("pytest")  # comment out if needed
    main()

