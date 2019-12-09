# Bubble Sort Ineficient

from typing import List
import random


def bubble_sort(nums: List[int]) -> List[int]:
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
                is_sorted = False
    

    return nums


print(
    
    bubble_sort([5, 3, 2, 1, 4]),
    bubble_sort([1, 2, 3, 4, 5]),
    sep = "\n"
)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(5):
    random.shuffle(numbers)
    print(numbers, bubble_sort(numbers[:]))



