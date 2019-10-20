# 2.py
# __init__ method

class Person:
    def __init__(self, name_in: str, age_in: int):
        self.name = name_in
        self.age = age_in


mr_beast_6000 = Person("Jimmy Donaldson", 21)
p = mr_beast_6000

print(f"Hello! Je m'appelle {p.name} et j'ai {p.age} ans")

print(f"Bonjour! Moi? Hon hon hon. Je suis {mr_beast_6000.name} et moi aussi, j'ai {mr_beast_6000.age} ans")