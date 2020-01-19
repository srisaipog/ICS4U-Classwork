from typing import List

def binary_search(nums: List[int], num: int) -> int:
    start = 0
    end = len(nums) - 1
    found = False

    while (start <= end) and (not found):
        mid = (start + end) // 2

        if nums[mid] < num:
            start = mid + 1
        elif nums[mid] > num:
            end = mid - 1
        elif nums[mid] == num:
            found = True
        else:
            raise Exception("How did we get here?")
    
    return mid


nums = [1, 3, 4, 5, 7, 8, 9, 11, 234, 5634, 345465]

for i in range(len(nums)):
    print(binary_search(nums, nums[i]))

