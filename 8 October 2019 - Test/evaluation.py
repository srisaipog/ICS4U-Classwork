# evaluation.py

from typing import List, Dict


def average_floats(a: float, b: float, c: float) -> float:
    """Gets the average of 3 floating point integers.

    Args:
        a: A float.
        b: A float.
        c: A float.
    Returns:
        Returns a float; the average of a, b and c.
    """

    return (a + b + c) / 3


def num_woods(woods: List, length: int) -> int:
    """Finds out how many times a specific length of wood appears in
       a list of wood lengths.

    Args:
        woods: A list of lengths of wood pieces.
        length: The length of the wood you want to search for.
    Returns:
        The number of times the given length appears in
        the list of wood lengths.
    """

    times = 0

    for wood in woods:
        if wood == length:
            times += 1

    return times


def board_list_dict(woods: List) -> Dict:
    """Uses the list of wood piece lengths to create
       a dictionary with the number of wood pieces for each length.

    Args:
        woods: A list of lengths of wood pieces.
    Returns:
        A dictionary with the key being the length of the wood piece
        and the value being the number of times the wood piece appears
        in the list
    """

    woody = {}

    for wood in woods:
        try:
            woody[wood] += 1
        except:
            woody[wood] = 1

    return woody


def num_woods_dict(woods: Dict, length: int) -> int:
    """Finds out how many pieces of wood of a specific length are
       there in the dictionary

    Args:
        woods: A dictionary with the number of each pieces for each wood length
    Returns:
        The number of wood pieces for the specified length
    """

    try:
        return woods[length]
    except:
        return 0
