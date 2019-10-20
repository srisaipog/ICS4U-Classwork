# Methods
# (Functions in classes are called methods)

class Person:
    def __init__(self, name: str, height: int, strength: int):
        self.name = name
    

    def introduce(self):
        print(f"My name is {self.name}. !ice 2 meat u")
    

    def compliment(self, peep):
        print(f"{peep.name}, I LoOoOvE your hair!")

p1 = Person("Jeff", 120, 10)
p2 = Person("Sally", 110, 5)

p1.introduce()
p1.compliment(p2)
