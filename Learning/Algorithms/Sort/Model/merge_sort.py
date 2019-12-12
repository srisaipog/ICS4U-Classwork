# Merge Sort

from typing import List
from random import shuffle


def merge_sort(nums: List[int]) -> List[int]:

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    
    left_side = merge_sort(nums[:mid])
    right_side = merge_sort(nums[mid:])
    
    sorted_list = []

    left_marker = 0
    right_marker = 0

    while (len(left_side) > left_marker) and (len(right_side) > right_marker):
        # put lists together

        if left_side[left_marker] < right_side[right_marker]:
            sorted_list.append(left_side[left_marker])
            left_marker += 1

        else: # left_side[left_marker] > right_side[right_marker] OR the values are equal
            sorted_list.append(right_side[right_marker])
            right_marker += 1
    
    # one list will be done, now to complete the other list

    while len(right_side) > right_marker:
        sorted_list.append(right_side[right_marker])
        right_marker += 1
    
    while len(left_side) > left_marker:
        sorted_list.append(left_side[left_marker])
        left_marker += 1

    return sorted_list # all done
    


nums = [0, 1, 2, 6, 4, 5, 3, 7, 8]

for i in range(15):
    shuffle(nums)
    print(merge_sort(nums[:]))