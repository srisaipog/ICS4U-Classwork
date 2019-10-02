import math

# Functions

def sum(nums: list) -> int:
    sum = 0
    
    for number in nums:
        sum += number
    
    return sum


# Testing Functions

def test_math_ceil():
    assert math.ceil(6.0001) == 7
    assert math.ceil(5.9) == 6


def test_sum():

    # assert True == False

    assert sum([]) == 0
    assert sum([1, 2, 3]) == 6
    assert sum([5, 5, 5]) == 15
    assert sum([2] * 2000) == 4000
    assert sum([1, 5, 6, 8, 999]) == 1019