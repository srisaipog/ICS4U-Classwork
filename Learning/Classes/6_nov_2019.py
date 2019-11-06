
# Function/Method overloading

# More of a java thing but can do in python as well

# Depending on what parameters you give, it will do that function

# Java Style
def draw_rectangle(x, y, w, h):
    pass


def draw_rectangle(x, y):
    pass


def draw_rectangle(x, y, color):
    pass

try:
    draw_rectangle(100, 150)
except TypeError:
    pass
# This will go to the second draw_rectangle as it takes 2 ints

# In Python, it will override the functions and you
# will end up with 1 draw_rectangle (the one at the end)
# draw_rectangle(x, y, color)


###############

# Python Style

import arcade


def draw_rectangle(x, y, w=100, h=100, color=arcade.color.BLUE):
    pass


draw_rectangle(50, 50) # draws rectangle at (50, 50) with w = 100, h = 100, color blue
draw_rectangle(100, 200, 5) # draws rectangle at (50, 50) with w = 5, h = 100, color blue
draw_rectangle(100, 400, 5, 6) # draws rectangle at (100, 400) with w = 5, h = 6, color blue
draw_rectangle(100, 400, 5, 6, arcade.color.WHITE) # draws rectangle at (100, 400) with w = 5, h = 6, color white
draw_rectangle(100, 200, arcade.color.WHITE) # Takes w = arcade.color.WHITE
draw_rectangle(100, 200, color=arcade.color.WHITE) # draws rectangle at (100, 200) with w = 100, h = 100, color white
draw_rectangle(x=69, y=430, color=arcade.color.BLACK) # easier to read
# order doesn't matter when you put the positional args
draw_rectangle(w=50, h=30, x=45, y=67)