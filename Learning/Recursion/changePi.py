"""
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".
changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
"""


def changePi(word: str) -> str:
    """Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".
    Args:
        word (str): The word to search in
    Returns:
        word (str) the new word with each instance of 'pi' replaced with '3.14'
    """

    if len(word) == 0 or len(word) == 1:
        return word
    
    if word[:2] == "pi":
        return "3.14" + changePi(word[2:])
    else:
        return word[0] + changePi(word[1:])


print(
changePi("xpix"),
changePi("pipi"),
changePi("pip"),
sep = "\n"
)