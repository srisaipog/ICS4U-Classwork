
class Person:
    
    def __init__(self, name: str, age: int):
        
        self.set_name(name)
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, to_be_age):
        if type(to_be_age) == int:
            self._age = to_be_age
    
    def get_name(self):
        return self._first_name + " " + self._last_name

    def set_name(self, to_be_name):
        if type(to_be_name) == str:
            first, last = to_be_name.split()
            self._first_name = first
            self._last_name = last
    


VOTING_AGE = 18

p = Person(name="Jeff Dickinson", age=22)


if p.get_age() >= VOTING_AGE:
    print(f"{p.get_name()} can vote")
else:
    print(f"{p.get_name()} can not vote")