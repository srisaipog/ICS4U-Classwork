class Person:
    pass


class Chair:
    """
    Attributes:
        num_legs:
        color:
        height: height in cm (int)
        occupant:
    """
    
    def __init__(self, color: str, num_legs: int, height: int):
        self.color = color # from the parameters
        self.num_legs = num_legs
        self.height = height
        self.occupant = None

    def __str__(self):
        # return ("u r a gr8 man")
        return f"This is a {self.color} chair"

c = Chair("Black", 5, 114) # c is a pointer to the object in memory
d = c

p = Person()

c.occupant = p

p.name = "Billy Bob Joe 3000"

c1 = Chair("Orange", 3, 551)
c2 = Chair("155, 226, 71", 4, 16)

print(c1)
print(c2)