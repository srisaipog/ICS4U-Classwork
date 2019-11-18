
# Linear search

"""
linear_search(target: int, numbers: List[int]) -> int

Returns:
    Index of the found target number. -1 for not found.

"""
from typing import List


# 1. Basic linear search.
# 2. Get last occurance of a balue.
# 3. Get list of all occurances.



def linear_search(target: int, numbers: List[int], search_type: str="basic") -> int:
    """
    Args:
        target (int): the number to find
        numbers (List[int]): a list of numbers to find the target
        search_type (str): The type of linear search (basic, last occurance, all occurances)
    Returns:
        The index of the target number. Returns -1 if not found
    """
    if search_type == "basic":
        for i in range(len(numbers)):
            if numbers[i] == target:
                return i
        else:
            return -1
    elif search_type == "last":
        last_index = -1
        for i in range(len(numbers)):
            if numbers[i] == target:
                last_index = i
        return last_index

    elif search_type == "all":
        indices = []
        for i in range(len(numbers)):
            if numbers[i] == target:
                indices.append(i)
        if len(indices) == 0:
            indices.append(-1)
        return indices

    else:
        return linear_search(target, numbers)

def test_linear_search():
    # Basic search
    assert linear_search(3, []) == -1
    assert linear_search(5, [5, 3, 6]) == 0
    assert linear_search(9, [0, 5, 6, 9]) == 3
    assert linear_search(7, [0, 6, 7, 9, 2]) == 2
    assert linear_search(6, [0, 6, 3, 6]) == 1

    # Last occurance search
    assert linear_search(3, []) == -1
    assert linear_search(5, [5, 3, 6], "last") == 0
    assert linear_search(9, [0, 5, 6, 9], "last") == 3
    assert linear_search(7, [0, 6, 7, 9, 2], "last") == 2
    assert linear_search(6, [0, 6, 3, 6], "last") == 3

    # All occurances search
    assert linear_search(3, [], "all") == [-1]
    assert linear_search(5, [5, 3, 6], "all") == [0]
    assert linear_search(9, [0, 5, 6, 9], "all") == [3]
    assert linear_search(7, [0, 6, 7, 9, 2], "all") == [2]
    assert linear_search(6, [0, 6, 3, 6], "all") == [1, 3]
    assert linear_search(7, [1, 7, 7, 7, 7, 0, 7], "all") == [1, 2, 3, 4, 6]


def test_structure():
    # Types of cases
    # list is empty
    # item is the first item
    # item is the last item
    # item is in the middle
    # item has multiple occurences.

    pass
