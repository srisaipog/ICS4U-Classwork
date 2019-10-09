
rick = ["Rick Sanchez", "blue", "0-01-01"]
# or
rick = {"name": "Rick Sanchez", "colour": "blue", "dob": "0-01-01"}

# Instead of storing things in a dict or a list
# Where you have to have an index, you can use a classs

# Instead of rick[0] or rick["name"]
# You can do this: rick.name

# Class names start with a capital letter and use camel case
# This is to differentiate with variables that use snake case
# and functions that also use snke case

# ex: class BobIsFat
# ex: def bob_eat_time

class Person:
    pass

blip = Person()

blip.name = "Rick"
print(blip.name)

Person.name = "MoOrtY"
print(Person.name)

class Scientist:
    name = "Rick"
    colour = "Blue"
    age = -1 # Infinity


print()
print()
print()

##################of making a class#############

# init method

# proper way 

class Person:
    # init wil run whenever you reference Person() with parentheses
    
    # This is a method because it is in a class
    # IF this was NOT in a class, it would be a function
    
    def __init__(self, n: str = "A Geeneeus", age: int = 0):
        # pass
        # print("MorTy! I made a PERSON!!!!!")
        # print(self)

        self.name = n

        self.age = age

        # print(f"Hello! I am {n} and i am {age} years old")
        # the age in self.age is not the same as the parameter age

# Person() is like a template while p and p2 are specific object instances

p = Person()
p2 = Person() # Same object, but stored in different memory addresses

mr = Person("Bethany", 40)

print(mr.name)
print(mr.age)

print(f"Hello! I am {mr.name} and i am {mr.age} years old")