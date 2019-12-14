"""
Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

contain_6([1, 6, 4], 0) → true
contain_6([1, 4], 0) → false
contain_6([6], 0) → true
"""

# lowercase true and false, lol

from typing import List

def contain_6(nums: List[int], index: int) -> bool:
    if len(nums) == index:
        return False
    
    if nums[index] == 6:
        return True
    else:
        return contain_6(nums, index + 1)


nums = [1, 2, 3, 2, 5]

import random

for _ in range(10):
    
    temp = []
    for _ in range(5):
        temp.append(random.randint(0, 10))
    
    print(temp, contain_6(temp, 0))
