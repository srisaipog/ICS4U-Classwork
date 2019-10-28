"""
1. Create a function that takes two integers a and b.
The function will return the sum of the two integers.

2. Create a function that takes a list of integers and returns the sum of all the numbers.

3. Create a function that takes a list of words.
Then create and return a dictionary where the key is 
the word and the value is how many times 
the word appears in the list.

"""
from typing import List, Dict

def add(a: int, b: int) -> int:
    """
    Create a function that takes two integers a and b.
    The function will return the sum of the two integers
    
    Args:
        a: An Integer
        b: another integer

    Returns:
        The sum of the two integers
    """

    return a + b


def add_list(nums: List) -> int:
    """
     Create a function that takes a list of
     integers and returns the sum of all the numbers.
    
    Args:
        nums: List of numbers
    
    Returns:
        sum: The sum of the list of numbers
    """

    sum = 0

    for num in nums:
        sum += num
    
    return sum


def num_times(words: List) -> Dict:
    """
    Create a function that takes a list of words.
    Then create and return a dictionary where the key is 
    the word and the value is how many times 
    the word appears in the list

    Args:
        words: A list of words
    
    Returns:
        word_count: A dict with the number of times
                    a word appears in the list "words"
    """

    word_count = {}

    for word in words:
       try:
           word_count[word] += 1
       except:
           word_count[word] = 1 
    
    return word_count


