"""
Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
array11([1, 2, 11], 0) → 1
array11([11, 11], 0) → 2
array11([1, 2, 3, 4], 0) → 0
"""

from typing import List

def array11(nums: List[int], index: int) -> int:
    if len(nums) < 0:
        return 0
    
    if index >= len(nums):
        return 0
    
    if nums[index] == 11:
        return 1 + array11(nums, index + 1)
    else:
        return array11(nums, index + 1)


def array11_better(nums: List[int]) -> int:
    if len(nums) < 1:
        return 0
    
    if nums[0] == 11:
        return 1 + array11_better(nums[1:])
    else:
        return array11_better(nums[1:])


print(

    array11([1, 2, 11], 0),
    array11([11, 11], 0),
    array11([1, 2, 3, 4], 0),
    sep="\n"

)

print(

    array11_better([1, 2, 11]),
    array11_better([11, 11]),
    array11_better([1, 2, 3, 4]),
    sep="\n"

)