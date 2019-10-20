# 1.py
# Store data in an object

class Person: # Creating (empty) class Person
    pass

jagmeet = Person() # Creating object of the class Person, jagmeet
jagmeet.name = "Jagmeet Singh" # Creating a variable name and giving it the value "Jagmeet Singh"
jagmeet.age = 40 # Creating a variable age and giving it the value 40
jagmeet.is_prime_minister = False # Creating a variable is_prime_minister and giving it the value False

p = jagmeet

print(f"Hello! My name is {p.name}. I am {p.age} years old.", end=" ")
if p.is_prime_minister:
    print("I am also the prime minister of Canada")
elif not p.is_prime_minister:
    print(f"I am not (yet) the prime minister of Canada")