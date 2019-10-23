# 1.py
"""
Person
======
name: str
height: int
strength: int
health_points: int = 100
---------
__str__(self) -> str
introduce(self) -> void
punch(Person) -> void
"""

class Person:
    """
    Attrs:
        height (int): in cm
        name (str): First and last
        strength (int): How strong the person is 
        health_points (int): Out of 100 (everyone starts at 100)
    """
    def __init__(self, name: str, height: int, sp: int, hp: int = 100):
        # self.name, self.height self.strength, self.health_points = name, height, sp, hp
        self.name = name
        self.height = height
        self.strength = sp
        self.health_points = hp
    

    def __str__(self):
        return f"Name: {self.name}, HP: {self.health_points}"
    

    def introduce(self):
        print(f"Hello, My name is {self.name}")
    

    def punch(self, someone):
        print(f"{self.name} punched {someone.name}")
        someone.health_points -= 10
    
    def eat(self):
        print(f"{self.name} eats!")
        self.health_points = 100


p1 = Person("Jerry", 150, 14)
p2 = Person("Larry", 110, 10)

print(p1)
print(p2)

p1.introduce()
p2.introduce()

p1.punch(p2)

print(p1)
print(p2)

p1.punch(p1)
print(p1)
p1.eat()

print(p1)
print(p2)