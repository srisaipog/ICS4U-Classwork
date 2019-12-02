"""
Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings should not overlap.
count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
"""

def count11(w: str, s: int = -1, e: int = -1, elevens: int = 0) -> int:
    if s == -1:
        s = 0
    if e == -1:
        e = 2
    
    try:
        if w[s:e] == '11':
            elevens += 1
            s += 2
            e += 2
        else:
            s += 1
            e += 1
        return count11(w, s, e, elevens)
    except:
        pass
    return elevens


print(
    count11("bob11smith11"),
    count11("11111111"),
    count11("11"),
    count11("111"),
    count11('1'),
    count11("abc11x11x11"),
    count11('11aa11'),

    sep = "\n"
)
