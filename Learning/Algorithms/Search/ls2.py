from typing import List

def ls(nums: List[int], num: int) -> int:
    for i in range(len(nums)):
        if nums[i] == num:
            return i
    else:
        return -1


ns = list(range(100))

print(

    ls(ns, -1),
    ls(ns, 0),
    ls(ns, 1),
    ls(ns, 4),
    ls(ns, 18),
    ls(ns, 50),
    ls(ns, 99),
    ls(ns, 100),
    ls(ns, 101),

    sep = "\n"

)