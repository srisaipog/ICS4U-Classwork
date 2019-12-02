
def bs(num, nums):
    start = 0
    end = len(nums) - 1
    mid = end

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


numss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bs(9, numss))