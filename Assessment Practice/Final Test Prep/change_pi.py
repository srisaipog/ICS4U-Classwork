"""
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".
changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
"""

def change_pi(word: str) -> str:
    if len(word) <= 1:
        return word
    
    if word[:2] == "pi":
        return "3.14" + change_pi(word[2:])
    else:
        return word[0] + change_pi(word[1:])


def changePi(word):
    return change_pi(word)

print(

    changePi("xpix"),
    changePi("pipi"),
    changePi("pip"),
    sep="\n"

)