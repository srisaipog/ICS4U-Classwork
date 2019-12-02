

def bs(num, nums):
    start = 0
    end = len(nums) - 1
    mid = end

    not_found = (end - start) <= 0

    while True:
        not_found = (end - start) <= 0

        if not_found:
            return -1
        
        if nums[mid] == num:
            return mid
        elif nums[mid] < num:
            start = mid
            mid = (start + end) // 2
        elif nums[mid] > num:
            end = mid
            mid = (start + end) // 2

numbers = list(range(69))

print(

    bs(0, numbers),
    bs(1, numbers),
    bs(2, numbers),
    bs(345, numbers),
    bs(49, numbers),
    bs(50, numbers),
    bs(51, numbers),
    bs(88, numbers),
    bs(99, numbers),
    bs(100, numbers),
    bs(5, numbers),
    bs(68, numbers),
    bs(69, numbers),

    sep = "\n"
)

