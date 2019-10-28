
'''

a = 5
b = a # Copies value a into b (not linked) [primative data types]

print(a, b) # 5 5

a = 10

print(a, b) # 10 5

print()
print()
print()

'''

# init has 2 underscores on each side (dunder (double underscore) method)

class Person:
    def __init__(self):
        pass

a = Person() # a is pointing towards Person(), a memory location
b = a

print(a, b)
print(a == b) # True

# Both a and b point to the same memory location

a.name = "Jeff"
print(b.name)
# They both point to the same name variable

del b # Deletes variable b
del a # Deletes variable a

# Now, no pointers to Person
# When garbage collection comes, it will check if there are any pointers
# If no pointers, deletes class

print(Person())

print(a, b)
