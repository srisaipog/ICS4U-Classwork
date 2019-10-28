class Person:
    """
    Attrs:
        height (int): in cm
        name (str): First and last
        strength (int): How strong the person is 
        health_points (int): Out of 100 (everyone starts at 100)
    """
    def __init__(self, name, height, strength):
        self.name = name
        self.height = height
        self.strength = strength
        self.health_points = 100
    
    def __str__(self):
        return f"{self.name}, hp: {self.health_points}"
    
    def introduce(self):
        print(f"Hello, my name is {self.name}")
    
    def punch(self, person):
        person.health_points -= 10


jeff = Person("Jeff Blah", 170, 1)
dave = Person("Dave Whitewall", 200, 1)

jeff.introduce()
dave.introduce()

print(jeff)
print(dave)

dave.punch(jeff)

print(jeff)
print(dave)
