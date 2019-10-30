"""
- Class field
- Class method

- Inheritance
"""

"""
Create the following Class:
"""

"""
Pizza
=====
name: str
topping: List[str]
-----
__str__ -> str


- Create a main function and create some pizzas!
- the __str__method will be the following format: "{name}, toppings: {toppings}"
"""
from typing import List


class Pizza():
    num_pizzas = 0 # class field (class variable)

    def __init__(self, name: str, toppings: List):
        self.name = name
        self.toppings = toppings
        self.id = Pizza.num_pizzas
        Pizza.num_pizzas += 1
    
    def __str__(self):
        tops = ""

        for topping in self.toppings:
            tops += (topping + ", ")
        
        tops = tops[:-2]

        return f"{self.name} | toppings: {tops} | id: {self.id}"
    
    def add_toppings(self, toppings_to_add: List):
        self.toppings += toppings_to_add


    @classmethod
    def create_pepperoni(cls): # self will automaticaly be sent as a class method
        # the var cls is the same as saying Pizza
        return cls("Pepperoni", ["cheese", "pepperoni"])

    # class method there just to help speed up the process   

    @classmethod
    def create_cheese(crass, extra_toppings: List=[]):
        return crass("Cheese", ["cheese"] + extra_toppings)




def main():
    pep = Pizza("Pepperoni", ["cheese", "pepperoni"])
    print(pep)
    print(Pizza.num_pizzas)
    # print(pep.num_pizzas)
    for _ in range(10):
        Pizza("Dicks Pizzaria", ['cheese', 'white sticky cheese'])
    
    print(Pizza.num_pizzas)
    print(pep.id)

    veg = Pizza("Veggie", ["Cheese", "Green Chillies"])
    print(veg)
    veg_2 = Pizza("Veggie", ["Cheese", "Green Chillies"])
    print(veg_2)

    print(Pizza.num_pizzas)

    ppap = Pizza.create_pepperoni()

    print(Pizza.num_pizzas)
    print(ppap)

    cheese_pee = Pizza.create_cheese()

    cheese_2 = Pizza.create_cheese(["American Cheese", "South American Cheese"])

    print(cheese_pee)
    print(cheese_2)

    cheese_2.add_toppings(["Asian Cheese", "Blue Cheese"])
    print(cheese_2)



if __name__ == "__main__":
    main()
