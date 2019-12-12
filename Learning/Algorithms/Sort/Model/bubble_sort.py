# Bubble Sort

import random

from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    is_sorted = False
    nums_left = len(nums) - 1

    while not is_sorted and nums_left >= 1:
        is_sorted = True
        for i in range(nums_left):

            is_sorted = False

            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


        nums_left -= 1
    
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

