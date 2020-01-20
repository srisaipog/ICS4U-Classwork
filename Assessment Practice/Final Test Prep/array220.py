"""
Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
array220([1, 2, 20], 0) → true
array220([3, 30], 0) → true
array220([3], 0) → false
"""

from typing import List

def array220(nums: List[int], index: int) -> bool:
    if index >= len(nums) - 1:
        return False
    
    if nums[index] * 10 == nums[index + 1]:
        return True
    else:
        return False or array220(nums, index + 1)

print(
    array220([1, 2, 20], 0),
    array220([3, 30], 0),
    array220([3], 0),
    sep="\n"
)