
from typing import List

def binary_search(nums: List[int], num: int):
    start = 0
    end = len(nums) - 1
    found = False

    while (start <= end) and (not found):
        mid = (start + end) // 2
    
        if nums[mid] < num:
            start = mid + 1  # + 1 IS VERY IMPORTANT
        elif nums[mid] > num:
            end = mid - 1 # -1 IS VERY IMPORTANT
        elif nums[mid] == num:
            found = True    

    return mid


# Testing

nuums = [1, 36, 40]

for i in range(len(nuums)):
    print(binary_search(nuums, nuums[i]))


