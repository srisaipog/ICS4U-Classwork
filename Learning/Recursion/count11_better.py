"""
Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings should not overlap.
count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
"""


def count11(word: str) -> int:
    """Counts all of the '11's in the string
    Args:
        word (str): the word to find the '11's in
    Returns:
        (int) the numbers of '11's in word
    """
    
    # Base Case
    if len(word) == 0 or len(word) == 1:
        return 0
    
    # Recursive Step
    if word[:2] == "11":
        return 1 + count11(word[2:])
    else:
        return 0 + count11(word[1:])



print(

    count11("211 11 11111"),
    count11("abc11x11x11"),
    sep = "\n"

)