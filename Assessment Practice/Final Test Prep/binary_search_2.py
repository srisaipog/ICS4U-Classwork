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
        elif num == nums[mid]:
            found = True
    
    return mid



nuums = [1, 3, 5, 7, 9, 11, 15, 18, 22, 26, 28, 33, 36, 40]

for i in range(len(nuums)):
    print(binary_search(nuums, nuums[i]))


