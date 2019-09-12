"""
Create a dictionary
Access dictionary values
Insert into dictionary
Modify dictionary values
Remove dictionary values
Loop over dictionary keys
Loop over dictionary values
Loop over dictionary values and keys
"""

grades = {"Sridhar": 100}

grades["Friend"] = 101

grades["Max"] = 100

grades.pop("Friend")

for name in grades:
    print(f"{name}: {grades[name]}")

grades["Max"] = 101

print()
print()

print(grades)

for name in grades.keys():
    grades[name] = None

for grade in grades.values():
    print(grade)

print(grades)

print(grades.values())
print(grades.keys())


exit()
quit()