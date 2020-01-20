# Binary Search
# Bubble Sort
# Merge Sort

from typing import List

def binary_search(nums: List[int], num: int) -> int:
    start = 0
    end = len(nums) - 1
    is_found = False

    while (start <= end) and (not is_found):
        mid = (start + end) // 2

        if nums[mid] < num:
            start = mid + 1
        elif nums[mid] > num:
            end = mid - 1
        elif nums[mid] == num:
            found = True
            return mid
    
    return -1


def test_search_algorithm(function):
    cur_search_algorithm = function
    nums = list(range(15))

    for i in range(len(nums)):
        print(cur_search_algorithm(nums, i))

    print(cur_search_algorithm(nums, 18))


def linear_search(nums: List[int], num: int) -> int:
    for i in range(len(nums)):
        if nums[i] == num:
            return i

    return -1


def bubble_sort(nums: List[int]) -> List[int]:
    nums_left = len(nums)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(nums_left - 1):
            a = nums[i]
            b = nums[i + 1]

            if a > b:
                nums[i] = b
                nums[i + 1] = a
                is_sorted = False
        
        nums_left -= 1

    return nums


def test_sort_algorithms(function):
    from random import shuffle
    nums = list(range(15))

    for i in range(len(nums)):
        shuffle(nums)

        print(function(nums))


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2

    left_side = merge_sort(nums[:mid])
    right_side = merge_sort(nums[mid:])

    left_counter = 0
    right_counter = 0

    sorted_list = []

    while (left_counter < len(left_side)) and (right_counter < len(right_side)):
        if left_side[left_counter] < right_side[right_counter]:
            sorted_list.append(left_side[left_counter])
            left_counter += 1
        else:
            sorted_list.append(right_side[right_counter])
            right_counter += 1
    
    while (left_counter < len(left_side)):
        sorted_list.append(left_side[left_counter])
        left_counter += 1
    
    while (right_counter < len(right_side)):
        sorted_list.append(right_side[right_counter])
        right_counter += 1
    
    return sorted_list



# test_search_algorithm(binary_search)
# test_sort_algorithms(bubble_sort)
# test_sort_algorithms(merge_sort)
# test_search_algorithm(linear_search)
