"""
Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the contents of the parenthesis, so "xyz(abc)123" yields "abc". Hint: have a recursive step going forward and a recursive step going backward.
only_inside("xyz(abc)123") → "abc"
only_inside("x(hello)") → "hello"
only_inside("(xy)1") → "xy"
"""


def only_inside(word: str) -> str:

    if len(word) == 0: return ""

    if word[0] == "(" and word[-1] == ")":
        return word[1:-1]
    
    if word[0] != "(":
        return only_inside(word[1:])
    if word[-1] != ")":
        return only_inside(word[:-1])


print(

    only_inside("apples"),
    only_inside("l am (bums) asdf"),
    only_inside("adsf(adsf"),
    only_inside("adsfasdf)fif"),
    only_inside("(tick)"),
    only_inside("(first) and (second)"),
    sep = "\n"

)


    