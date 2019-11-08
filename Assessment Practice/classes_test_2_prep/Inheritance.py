# Inheritance

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    @staticmethod
    def speak():
        print("Generic animal sounds")


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
    
    @staticmethod
    def speak():
        print("Woof")
    


def main():
    d = Dog("Fido", 45, "Mutt")
    d.speak()

    an = Animal("Generic", 345)
    an.speak()


if __name__ == "__main__":
    main()