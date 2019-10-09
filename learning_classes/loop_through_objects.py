class Person:
    def __init__(self, n: str = "u smart", age: int = 323424):
        self.name = n
        self.age = age


# Not a good way to store variables. use a list or something
'''
p1 = Person("bob", 234)
p2 = Person()
p3 = Person("smith")
p4 = Person()

people = [p1, p2, p3, p4]

for peep in people:
    print(peep.name, peep.age)
(

# OROROROROROROROR


# This only makes 1 variable
people = [
    Person("bob", 12345123),
    Person(),
    Person("Smith JR."),
    Person(),
]

'''

person = []

for name, age in [("Jeff", 234), ("Smith", 15), ("rig", -1)]:
    p = Person(name, age)
    person.append(p)

for aa in person:
    print(aa.name)
