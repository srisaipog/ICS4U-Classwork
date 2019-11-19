"""
# Linear search exercises

1. Search a list of ints for a particular integer. Return the index location, -1 if not found.
2. Search a list of ints for the last occurance of a particular integer. -1 if not found.
3. Search a list of ints for every occurance of a particular integer. Return a list of every index number. Empty list if not found.
4. Search a list of strings for words that start with a substring. Return the first occurance index.
5. Search a list of strings for words that start with a substring. Return list of all the strings (not the index positions).

"""

from typing import List

def exercise_1(num_to_find: int, list_of_nums: List[int]) -> int:
    """
    Search a list of ints for a particular integer.
    Return the index location, -1 if not found.

    Args:
        num_to_find (int): The number to search for
        list_of_nums (List[int]): A list of numbers
    Returns:
        The index of num_to_find in list_of_nums.
        If num_to_find is not found in list_of_nums, returns -1
    """
    for i in range(len(list_of_nums)):
        if list_of_nums == num_to_find:
            return i
    else:
        return -1


def exercise_2(num_to_find: int, list_of_nums: List[int]) -> int:
    """
    Search a list of ints for the last occurance of a particular integer.
    Returns the index location, -1 if not found.

    Args:
        num_to_find (int): The number to find
        list_of_nums (List[int]): A List of numbers
    Returns:
        The last index of num_to_find in list_of_nums.
        Returns -1 if not found
    """
    index = -1
    for i in range(len(list_of_nums)):
        if list_if_nums[i] == num_to_find:
            index = i
        
    return index


def exercise_3(num_to_find: int, list_of_nums: List[int]) -> List[int]:
    """
    Search a list of ints for every occurance of a particular integer.
    Return a list of every index number. Empty list if not found.

    Args:
        num_to_find (int): the number to find
        list_of_nums (List[int]): a list of numbers
    Returns:
        A list of indexes where the number is found in the list.
        Returns an empty list if the number is not found
    """

    indices = []

    for i in range(len(list_of_nums)):
        if list_of_nums[i] == num_to_find:
            indices.append(i)
    
    return indices


def exercise_4(string_to_find: str, list_of_strings: List[str]) -> int:
    """
    Search a list of strings for words that start with a substring.
    Return the first occurance index.

    Args:
        string_to_find (str): The substring to find in the list
        list_of_strings (List[str]): The list of strings
    Returns:
        Returns the first occurance of where the string in
        list_of_strings starts with string_to_find
    """

    for i in range(len(list_of_strings)):
        if list_of_strings[i].startswith(string_to_find):
            return i
    else:
        return -1


def exercise_5(string_to_find: str, list_of_strings: List[str]) -> List[str]:
    """
    Search a list of strings for words that start with a substring.
    Return list of all the strings (not the index positions).
    
    Args:
        string_to_find (str): the string to find
        list_of_strings (List[str]): a list of strings
    Returns:
        list of all the strings
    """
    strings_to_return = []

    for word in list_of_strings:
        if word.startswith(string_to_find):
            strings_to_return.append(word)
    
    return strings_to_return

