# Classes Quiz Prep.py

"""
Topics:

Annotate class and methods
Docstrings for Class and methods
Store data in an object
__init__ method
Loop through a list of objects
Understand object pointers
Know difference between a class and an object
Instance method
"""

# 1
"""
Create an Item class with the following details:

Food
====
name: str
cost: int
nutrition: int
"""

class Food:
    def __init__(self, name: str, cost: int, nutrition: int):
        self.name = name
        self.cost = cost
        self.nutrition = nutrition

#2
"""
Create a Dog class with the following details:

Dog
====
breed: str
name: str
happiness: int
-----
__str__() -> str
eat(Food) -> void
bark() -> void
"""

class Dog:
    def __init__(self, breed: str, name: str, happiness: int):
        self.breed = breed
        self.name = name
        self.happiness = happiness

    
    def __str__(self):
        return f"{self.name} has {self.happiness} happiness"


    def eat(self, food):
        self.happiness += 0.1 * food.nutrition

    
    def bark(self, times: int = 1):
        for i in range(times):
            print("RUFF RUFF!")


def main():
    klondike = Dog("Toy American Eskimo", "Klondike", 720)
    sundae = Dog("Toy American Eskimo", "Sundae", 230)
    kermit = Dog("Italian Greyhound", "Kermit", 5)

    steak = Food("Steak", 5, 15)
    beef = Food("Beef", 3, 10)
    chocolate = Food("Chocolate", 5, -9999999999999)

    klondike.eat(steak)
    sundae.eat(beef)

    print(klondike)
    print(sundae)

    kermit.eat(beef)
    kermit.bark()

    print(kermit)

    kermit.eat(chocolate)
    kermit.bark(10)

    print(kermit)

    print()

    print("Final:")
    print(klondike)
    print(sundae)
    print(kermit)


if __name__ == "__main__":
    main()