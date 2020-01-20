"""
Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.
changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
"""


def changeXY(word: str) -> str:
    if len(word) < 1:
        return word

    if word[0] == "x":
        return "y" + changeXY(changeXY(word[1:]))
    else:
        return word[0] + changeXY(changeXY(word[1:]))

print(
    changeXY("codex"),
    changeXY("xxhixx"),
    changeXY("xhixhix"),
    sep = "\n"
)
