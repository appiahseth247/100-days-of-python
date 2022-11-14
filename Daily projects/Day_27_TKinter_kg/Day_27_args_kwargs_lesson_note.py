
# TODO NOTE1: Advanced Python Arguments


# Default values assigned to arguments (=...) when creating a function can be modified when calling the function
# unless the argument is required
#
# def my_function(a=2, b=4, c=0):
#     print(a, b, c)
#
#
# my_function(b=88)


# NOTE2: creating a function that can an unlimited number of POSITIONAL arguments
def add(*args):  # The asterisk(*) is used to tell python that this function can accept any number of arguments
    print(args, type(args))  # A tuple
    print(args[0])  # You can index through it as well
    total_sum = 0
    for n in args:  # You can loop through the args which will be a form of a tuple
        total_sum += n  # And do whatever you want with the args. The name "args" is the default name used by
        # developers but you can change it to whatever name you want
    return total_sum


print(add(2, 3, 5, 6, 66))
print(add(233, 3))


# NOTE#: creating a function that can an unlimited number of KEYWORD arguments
def calculate(n, **kwargs):  # ** means the function can take unlimited number  of  kwargs (keyword arguments)
    print(kwargs, type(kwargs))  # A dictionary
    for key, value in kwargs.items():  # Loop through like a dictionary
        print(key, value, kwargs["add"])
    n += kwargs["add"]  # To get the value under "add"
    n *= kwargs["multiply"]
    print(n)


calculate(44, add=3, multiply=9)


class Car():
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")  # get() can also be used to get hold of values in a dict just like the ["key"]
        self.owner = kwargs.get("owner")  # The benefit of get() is that it returns 'none' instead of an error
        # if the key doesn't exit in the dictionary


my_car = Car(make="Nisan", model="GT-R")
print(my_car.model)
