'''
Given a string, compute recursively a new string where all the adjacent chars are now separated by a given character.
sep_char("hello", "*") → "h*e*l*l*o"
sep_char("abc", ".") → "a.b.c"
sep_char("ab", "/") → "a/b"

'''

def sep_char(word: str, sep: str) -> str:
    if len(word) <= 1:
        return word
    else:
        return word[0] + sep + sep_char(word[1:], sep)




letters = 'abcdefghijklmnopqrstuvwxyz'

symbols = "!@#$%^&*()"


from random import choice

for i in range(10):
    word = ""
    for i in range(5):
        word += choice(letters)
    symbol = choice(symbols)

    print(word, symbol, sep_char(word, symbol))

