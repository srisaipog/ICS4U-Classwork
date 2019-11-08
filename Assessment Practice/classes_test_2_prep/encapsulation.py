# Encapsulation

class Person:
    def __init__(self, name: str, age: int, gender: str):
        self._name = name
        self._age = age
        self._gender = gender
    
    def get_age(self) -> str:
        return f"Age: {self._age}"
    
    def set_age(self, age: int) -> None:
        if (type(age) is int):
            if (age >= 0):
                self._age = age
            else:
                raise TypeError("Age must be a positive integer")
        else:
            raise TypeError("Age must be a positive integer")
    
    def get_gender(self) -> str:
        return f"Gender: {self._gender}"
    
    def set_gender(self, gender: str) -> None:
        self._gender = gender


def main():

    s = Person("Sridhar", 43, "Male")
    print(s.get_age())
    print(s.get_gender())
    s.set_age(5)
    print(s.get_age())
    s.set_gender("Man")
    print(s.get_gender())
    s.set_age(-1)
            
if __name__ == "__main__":
    main()