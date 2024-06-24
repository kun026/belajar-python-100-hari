""" Arguments with Default Values
def my_function(a=1, b=2, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this wich c

my_function()
my_function(b=5)
"""

# *args: many positional arguments; Unlimited Positional Arguments; type args is tuple
# *args: Positional Variable-Length Arguments
# * : unpacking operator
def add(*nums):
    sum = 0
    for n in nums:
        sum += n
    
    return sum

result = add(1,2,3,4,5)
# print(result)

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Prof.", "Dr.", "Ridho", "Syam")

# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)