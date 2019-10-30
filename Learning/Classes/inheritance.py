"""
Cat
===
name: str
breed: str
-----
speak() -> void


Dog
===
name: str
breed: str
-----
speak() -> void
"""

class Animal:
    sound = "Generic Animal Sounds.wav"

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    @classmethod
    def speak(cls):
        print(cls.sound)


class Cat(Animal):

    sound = "MEOW"

    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed
    
    def __str__(self) -> str:
        return super().__str__() + f", {self.breed}"

    @staticmethod
    def meow():
       print(Cat.sound)
    
class Dog(Animal):

    sound = "RUFF"

    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed
    
    def __str__(self) -> str:
        return super().__str__() + f", {self.breed}"

    @staticmethod
    def bark():
        print(Dog.sound)

class Chipmunk(Animal):
    sound = "*eats nut*"


def main():
    d = Dog("Fluffy", "Husky")
    print(d)
    d.bark()

    c = Cat("Jerry Smith", "Pussy Cat")
    print(c)
    c.meow()

    chip = Chipmunk("Alvin")
    chip.speak()

    c.speak()
    d.speak()

    print(chip)


if __name__ == "__main__":
    main()