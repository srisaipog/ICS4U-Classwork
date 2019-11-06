"""

- Create a main function to showcase all the functionality.
- Encapsulate ALL object fields with getters/setters.

Notes
Person:
- make email a default optional parameter in the initializer. Make the default None.
- Do not make a setter for the DOB.

Teacher:
- The assign_work method will just print something out. Include the teacher name and class name.
- Ensure you cannot add more than 6 classes to a Teacher with the add_class method.

Class_:
- Create a class variable, a list of flags or warnings. When a class exceeds 33 students, a warning is created in the Class_ class.
- Raise an error if you attempt to remove a student from a class who wasn't in the class to begin with.

Extend the program
- Create a School class, make modifications to Teacher and Student.
- Create a all_teachers field for the Teachers class. Make @classmethod to search for a teacher by their OCT_PIN. Make another @classmethod to search for a teacher by their last name.

"""

# Test file link
# https://gist.github.com/MrGallo/12aff3c2f6e71138796c51b82afdaccd

from datetime import datetime

class Person:
    def __init__(self, first_name: str, last_name: str, email: str=None, DOB: datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.DOB = DOB


class Teacher:
    pass


class Class_:
    pass