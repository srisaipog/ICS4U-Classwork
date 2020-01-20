"""
Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
"""


def allStar(word: str) -> str:
    if len(word) <= 1:
        return word
    
    return word[0] + "*" + allStar(word[1:])




print(

    allStar("hello"),
    allStar("abc"),
    allStar("ab"),
    sep = "\n"
)