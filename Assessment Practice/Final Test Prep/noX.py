"""
Given a string, compute recursively a new string where all the 'x' chars have been removed.
noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
"""

def noX(word: str) -> str:
    if len(word) < 1:
        return word
    
    if word[0] == "x":
        return noX(word[1:])
    else:
        return word[0] + noX(word[1:])


print(

    noX("xaxb"),
    noX("abc"),
    noX("xx"),

    sep="\n"
)