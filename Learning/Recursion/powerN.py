"""
Given <b>base</b> and <b>n</b> that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27
"""


def powerN(b: int, p: int) -> int:
    if p == 0:
        return 1
    elif p == 1:
        return b
    return b * powerN(b, p-1)


print(powerN(8, 3))