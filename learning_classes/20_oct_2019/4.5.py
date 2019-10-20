# 4.5.py
# Understand object pointers
# For, objects the memory location (pointer) is stored in variables.

class Person:
    pass

a = Person()

a.name = "Isaac"
print(a.name)

a.age = -1
print(a.age)

print()

b = a
print(b.name)
print(b.age)

print()

# Both variables point to the same object in memory
print(a)
print(b)

print()
a.age = 987654
b.name = "New Tonne"

print(b.age)
print(a.name)