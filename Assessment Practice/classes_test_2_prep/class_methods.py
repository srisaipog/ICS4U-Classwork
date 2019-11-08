# Class Methods

class Person():
    people = []

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        Person.people.append(self)
    
    @classmethod
    def flamboy(cls):
        cls("Richarde", 25, "Memale")
    
    @classmethod
    def generic_male(cls):
        cls("John Smith", 36, "Male")
    
    @classmethod
    def generic_female(cls):
        cls("Mary Janes", 38, "Female")

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


def main():
    s = Person("Sridhar", 16, "Male")
    fe = Person.generic_female()
    ma = Person.generic_male()
    gay = Person.flamboy()

    for person in Person.people:
        print(person)


if __name__ == "__main__":
    main()