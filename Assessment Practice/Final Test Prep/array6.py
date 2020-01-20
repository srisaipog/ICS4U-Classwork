"""
Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
array6([1, 6, 4], 0) → true
array6([1, 4], 0) → false
array6([6], 0) → true
"""

from typing import List

def array6(nums: List[int], index: int) -> bool:
    if len(nums) < 1:
        return False
    
    if index >= len(nums):
        return False
    
    if nums[index] == 6:
        return True
    else:
        return False or array6(nums, index + 1)


def array6_better(nums: List[int]) -> bool:
    if len(nums) < 1:
        return False
    
    if nums[0] == 6:
        return True
    else:
        return False or array6_better(nums[1:])

'''
print(
    array6([1, 6, 4], 0),
    array6([1, 4], 0),
    array6([6], 0),
    sep="\n"
)
'''
print(
    array6_better([1, 6, 4]),
    array6_better([1, 4]),
    array6_better([6]),
    sep="\n"
)