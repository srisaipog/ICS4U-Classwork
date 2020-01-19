from typing import List

def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_side = merge_sort(nums[:mid])
    right_side = merge_sort(nums[mid:])

    left_counter = 0
    right_counter = 0
    sorted_list = []

    while (left_counter < len(left_side)) and (right_counter < len(right_side)):
        if left_side[left_counter] < right_side[right_counter]:
            sorted_list.append(left_side[left_counter])
            left_counter += 1
        else:
            sorted_list.append(right_side[right_counter])
            right_counter += 1
    
    while left_counter < len(left_side):
        sorted_list.append(left_side[left_counter])
        left_counter += 1
    
    while right_counter < len(right_side):
        sorted_list.append(right_side[right_counter])
        right_counter += 1
    
    return sorted_list

import random

print(merge_sort([1, 2, 3, 4, 5]))
print(merge_sort([5, 4, 3, 2, 1, 0]))
print(merge_sort([random.randrange(100) for _ in range(10)]))