
# Linear search

"""
linear_search(target: int, numbers: List[int]) -> int

Returns:
    Index of the found target number. -1 for not found.

"""


def linear_search(target: int, numbers: List[int]) -> int:
    """
    Args:
        target (int): the number to find
        numbers (List[int]): a list of numbers to find the target
    Returns:
        The index of the target number. Returns -1 if not found
    """

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    else:
        return -1


