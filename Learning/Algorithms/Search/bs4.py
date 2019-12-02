
from typing import List

def bs(nums: List[int], num: int) -> int:
    start = 0
    end = len(nums) -1
    mid = end
    not_found = (end - start) <= 0

    while True:

        not_found = (end - start) <= 0

        if not_found:
            return -1

        if nums[mid] == num:
            return mid
        elif nums[mid] > num:
            end = mid
            mid = (start + end) // 2
        elif nums[mid] < num:
            start = mid
            mid = (start + end) // 2

ns = list(range(100))

print(

    bs(ns, 0),
    bs(ns, 1),
    bs(ns, 6),
    bs(ns, 48),
    bs(ns, 49),
    bs(ns, 50),
    bs(ns, 51),
    bs(ns, 99),
    bs(ns, 100),
    bs(ns, 101),
    bs(ns, -1),

    sep = "\n"

)