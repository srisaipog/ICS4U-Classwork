
from typing import List

def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2

    left_side = merge_sort(nums[:mid])
    right_side = merge_sort(nums[mid:])

    sorted_list = []
    left_marker = 0
    right_marker = 0

    while len(left_side) > left_marker and len(right_side) > right_marker:
        # put them into the sorted list one by one

        if left_side[left_marker] > right_side[right_marker]:
            sorted_list.append(right_side[right_marker])
            right_marker += 1
        else:
            sorted_list.append(left_side[left_marker])
            left_marker += 1
        
    # do the rest of the nums

    # only 1 of these while loops will actuall run

    while len(left_side) > left_marker:
        sorted_list.append(left_side[left_marker])
        left_marker += 1
    
    while len(right_side) > right_marker:
        sorted_list.append(right_side[right_marker])
        right_marker += 1
    
    return sorted_list


bums = [9, 594, 3, 4, 2, 4, 1, 3, 6, 1, 0]

print(merge_sort(bums))