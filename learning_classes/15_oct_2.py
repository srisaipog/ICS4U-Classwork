class Person:
    """
    Attributes:
        name (str): first and last
        height (int): in cm
        strength (int): How strong the person is
        health_points (int): Out of 100

    """

    def __init__(self, name: str, height: int, strength: int,
                 health_points: int = 100):
        self.height = height
        self.name = name
        self.strength = strength
        self.health_points = strength
    
    def __str__(self):
        return f"{self.name} has {self.health_points} health points and {self.strength} strength points and is {self.height} cm tall"

    def introduce(self):
        print(f"Hello, mera naam {self.name}")

    def punch(self, person):
        person.health_points -= 10
    
    def eat(self):
        self.health_points += 10


kill_points = 100

kill_points -= 10

max = Person("Max N", 255, 420)

# Gives potion to max
max.health_points += 100
# print(max.health_points)

# Max gets whooped in the face
max.health_points -= 469
# print(max.health_points)

# print(max)


jim = Person("Mr Beast 6000", 100, 32415)

max.introduce()
jim.introduce()

print(jim)
print(max)

max.punch(jim)

print(jim)
print(max)

# Max goes to a buffet
for i in range(2346):
    max.eat()

print(jim)
print(max)
