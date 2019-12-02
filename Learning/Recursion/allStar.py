'''
Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
'''

def allStar(w: str, mode=-1) -> str:
    if len(w) == 1:
        return w + "*"
    else:
        bob = allStar(w[:-1], 0) + allStar(w[-1], 0)
    if mode == -1:
        return bob[:-1]
    else:
        return bob


print(
    
    allStar("Jerry"),
    allStar("Beth"),
    allStar("meth"),

    sep = "\n"

)