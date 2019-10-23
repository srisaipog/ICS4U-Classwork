"""

ENCAPSULATION:

Basic definition: protecting your object;s attributes

"""


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

    def set_age(self, age: int): # setter
        # Verify that the value is an int
        
        if type(age) != int:
            raise ValueError("Age must be an Integer")

        self._age = age

    def get_age(self): # getter
        return self._age


s = Student("Smith", 5)

# We don't want people to do this.
# s.set_age(False)
# s.set_age(False) # raises an error

# s.age is still accessable. to make it private, make it self._age

s.age = "adf" # creates a new variable s.age
s._age = "3sf3gs" # rewrites s._age

print(s.get_age())
print(s.name)