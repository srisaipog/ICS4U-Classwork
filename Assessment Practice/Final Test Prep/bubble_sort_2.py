from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    items_left = len(nums)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(items_left - 1):
            a = nums[i]
            b = nums[i + 1]

            if a > b:
                nums[i] = b
                nums[i + 1] = a
                is_sorted = False
        
        items_left -= 1
    
    return nums


from random import shuffle

nums = list(range(15))

for i in range(10):
    shuffle(nums)
    print(bubble_sort(nums))
    
