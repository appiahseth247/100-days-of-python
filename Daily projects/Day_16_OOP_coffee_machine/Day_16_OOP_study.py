from turtle import Turtle, Screen
from prettytable import PrettyTable

# method = a function associated with an object : object.methodname()
# attributes = variable associated with an object : object.attributename

# Creating a new object called tortoise using a class called Turtle() which is from a module called turtle
tortoise = Turtle()
print(tortoise)
tortoise.shape("turtle")
tortoise.color("coral")
tortoise.forward(50)
print(tortoise.position())

my_screen = Screen()  # Creating a new object called my_screen from a class called Screen()
print(my_screen.canvheight)  # this attribute is used to check the height of the screen created
my_screen.exitonclick()  # This method will allow Created screen remain until there is a click

table = PrettyTable()
# add_column is a method, which means it's a function associated with the table object.
# Functions still need to be called with a ()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# align is a attribute which means it's a variable associated with the table object.
# values are assigned to variables using the = sign
table.align = "l"

print(table.align)  # the align attribute can be printed out just any variable
print(table)
