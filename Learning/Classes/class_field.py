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




if __name__ == "__main__":
    main()
