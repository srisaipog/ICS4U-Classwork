"""
Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
"""

def count_hi(word: str) -> int:
    # Base Case
    if len(word) <= 1:
        return 0
    
    # Recursive Step
    if word[:2] == "hi":
        return 1 + count_hi(word[2:])
    else:
        return 0 + count_hi(word[1:])
    


test_words = "hiyouhitard iliketohike ihavethebigsasd hihei".split()

for word in test_words:
    print(count_hi(word))