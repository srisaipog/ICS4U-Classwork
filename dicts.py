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

for grade in grades:
    print(str(grade) + ":", grades[grade])

print()
print()

print(grades)
    