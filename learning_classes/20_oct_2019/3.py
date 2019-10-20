# 3.py
# Loop through a list of objects

class Person:
    def __init__(self, nom: str, age: int):
        self.name = nom
        self.age = age


# Creates person objects in variables
jimmy = Person("Jimmothy", 25)
sri = Person("Sridhar", 16)
morty = Person("Morty Smith", 14)
rick = Person("Rick Sanchez", 42069)

# Puts variables in list
people = [jimmy, sri, morty, rick]

# Creates person objects in the list directly (better)
# Saves space and time

peoples = [
    Person("Jimmothy", 25),
    Person("Sridhar", 16),
    Person("Morty Smith", 14),
    Person("Rick Sanchez", 42069)
]

for person in people:
    print(f"Hello ma doodes! You can call me {person.name} and I'm {person.age} years old so you best respect me!")

print()

for p in peoples:
    print(f"Hello ma doodes! You can call me {p.name} and I'm {p.age} years old so you best respect me!")

print(people == peoples) # False
print(people is peoples) # False