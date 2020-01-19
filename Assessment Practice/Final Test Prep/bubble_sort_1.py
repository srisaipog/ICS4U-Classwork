from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    items_left = len(nums)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(items_left - 1):
            a = nums[i]
            b = nums[i + 1]

            if a > b:
                nums[i + 1] = a
                nums[i] = b
                is_sorted = False
            
        items_left -= 1

    return nums



import random

print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1, 0]))
print(bubble_sort([random.randrange(100) for _ in range(10)]))