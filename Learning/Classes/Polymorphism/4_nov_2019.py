'''
Person
======
- first_name (str)
- last_name (str)
- dob (DateTime)
-----------
+ greet() -> str
+ get_age() -> int
'''

class Person():
    def __init__(self, first_name: str, last_name: str, dob: DateTime):
        self._first_name = first_name
        self._last_name = last_name
        self._dob = dob


'''
Teacher
=======
- OCT_PIN: int
- school: str
- classes: List[class]
----------

assign_work(class) -> void
greet() -> void
'''


'''
Class_
=====

- subject: str
- students: List[student]

'''


'''
Student
=======

- email_k12: str
- student_number: int
-------

greet() -> void


'''