# Second week 2 part

# Exceptions...
print("Try and Except")
"""In Python, the try and except blocks are used for error handling, 
allowing you to gracefully manage exceptions that might occur during the execution of your code. """
#
"""
try :
    # statements in try block
except :
    # executed when exception occurred in try block    
"""
#
"""try:
    # Code that may raise an exception
    # ...
except ExceptionType:
    # Code to handle the specific exception
    # ...
except AnotherExceptionType:
    # Code to handle another specific exception
    # ...
except:
    # Code to handle any other type of exception
    # ...
else:
    # Optional block that executes if no exception occurs
    # ...
finally:
    # Optional block that always executes, regardless of whether an exception occurred
    # ...
"""
try:
    a = 10
    b = 0
    c = a / b
    print("The answer of a divided by b is :", c)

except:
    print("can not divide by 0")  # output is this

try:
    # a = int(input("Enter the value of a: "))
    # b = int(input("Enter the value of b: "))
    c = a / b
    print("the answer of a divided by b: ", c)
except ValueError:
    print("Entered value wrong")  # if i enter a instead int
except ZeroDivisionError:
    print("Can't divide by zero ")

# Merging
print("Merging the excepts")
try:
    # a = int(input("Enter the value of a: "))
    # b = int(input("Enter the value of b: "))
    c = a / b
    print("the answer of a divided by b: ", c)
except(ValueError, ZeroDivisionError):  # merging the excepting
    print("Enter a valid value")

print("finally")
# finally that always execute weather error occurs or not
try:
    # a = int(input("Enter the value of a: "))
    # b = int(input("Enter the value of b: "))
    c = a / b
    print("the answer of a divided by b: ", c)
except(ValueError, ZeroDivisionError):  # merging the excepting
    print("Enter a valid value")  #
finally:
    print("inside a finally block")

# else : if there is not exception then it will execute
print("else : ")

try:
    # a = int(input("Enter the value of a: "))
    # b = int(input("Enter the value of b: "))
    c = a / b
    print("the answer of a divided by b: ", c)
except(ValueError, ZeroDivisionError):  # merging the excepting
    print("Enter a valid value")  #
else:
    print("everything is fine")

print("raising the error ")


# faiz
def simple_interest(amount, year, rate):
    try:
        if rate > 100:
            raise ValueError(rate)
        interest = (amount * year * rate) / 100
        print("the simple interest is: ", interest)
        return interest
    except ValueError:
        print("Interest rate is out of range:", rate)


print("case 1")
simple_interest(800, 6, 8)
print("case 2")
simple_interest(800, 6, 800)

print("*args and **kwargs")


# *args collects positional arguments into a tuple
def example_function(*args):
    print("Positional arguments:", args)


# **kwargs collects keyword arguments into a dictionary
def another_function(**kwargs):
    print("Keyword arguments:", kwargs)


# Example usage
example_function(1, 2, 3)
another_function(name='Alice', age=30)


def MyFunction(arg1, *args):
    print("First argument is:", arg1)
    print("Next arguments through:")
    for arg in args:
        print(arg)


MyFunction('Hello', 'Welcome', 'to', 'python')  # Output:


# First argument is: Hello
# Next arguments through:
# Welcome
# to
# python

# Or dklfvmdflkv
def MyFunction(arg1, *args):
    print("First argument is:", arg1)
    printed_next = False
    for arg in args:
        if arg == 'Welcome':
            print("Next arguments through:")
            printed_next = True
            print(arg)
        elif printed_next:
            print(arg)


MyFunction('Hello', 'Welcome', 'to', 'python')  # Output:


# First argument is: Hello
# Next arguments through:
# Welcome
# to
# python

# Using the **kwargs
def Myfunction(**kwargs):
    print(kwargs)  # print all
    for key, value in kwargs.items():  # print separately
        print("%s : %s" % (key, value))


Myfunction(name='Ahmet', lastname='Akdag', year='2001')

print("using the *args and **kwargs to pass the fuction")


def myFucntion(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)


arg = ('Welcom', 'to', 'Python')
myFucntion(*arg)
kwargs = {'arg1': 'Welcom', 'arg2': 'to', 'arg3': 'Python'}
myFucntion(**kwargs)
# output
# arg1:  Welcom
# arg2:  to
# arg3:  Python

print("using *args and **kwargs together")


def Myfunction(*args, **kwargs):
    print("args :", args)
    print("kwargs :", kwargs)


Myfunction('hello', 'my', 'python', first='hellow', mid='my', last='python')
# output
"""args : ('hello', 'my', 'python')
kwargs : {'first': 'hellow', 'mid': 'my', 'last': 'python'}"""


class Car:
    def __init__(self, *args):
        self.speed = args[0]
        self.color = args[1]


audi = Car(200, 'red')
bmw = Car(300, 'blue')
print(audi.color)
print(bmw.speed)
bmw1 = Car(300, 'black')
print(bmw1.color)  # black


class Car:
    def __init__(self, **kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']


audi = Car(c=200, s='red')
bmw = Car(c=300, s='blue')
print(audi.color)  # 200
print(bmw.speed)

print("decorator in python")


def message(text):
    return text.upper()


print(message('hello'))  # HELLO
newmessage = message  # the memory addresses are same
print(newmessage('Hello'))  # HELLO


# FUNCTION CAN BE PASSED AS ARGUMENT TO OTHER FUNCTION
def message1(text):
    return text.upper()


def message2(text):
    return text.lower()


def greet(func):
    greeting = func("Hello, this is test message")
    print(greeting)


greet(message1)  # HELLO, THIS IS TEST MESSAGE
greet(message2)  # hello, this is test message


# returning function from another function
def creat_adder(x):
    # Define a function adder(y) which takes one argument y
    def adder(y):
        # Return the sum of x (captured from the outer scope) and y
        return x + y

    # Return the inner function adder
    return adder


# Call creat_adder(15) and store the returned function in add_15
add_15 = creat_adder(15)  # x = 15

# Call the function add_15 with argument 10, resulting in 15 + 10 = 25
print(add_15(10))  # Output: 25


# using function in other function

def increas(x):
    return x + 1


def decreas(x):
    return x - 1


def operation(func, x):
    result = func(x)
    return result


print(operation(increas, 4))  # 5
print(operation(decreas, 4))  # 3


def calling():
    def returned():
        print("helloo")

    return returned()


new = calling()  # helloo


# new()   not need to call

# adding extra properties to a function by another function using @
def new_divide(func):
    def inner(a, b):
        print("Divide", a, "and", b)
        if b == 0:
            print("can not divide by zero")
            return
        return func(a, b)

    return inner


@new_divide
def Divide(a, b):
    return a / b


Divide(1, 0)  # can not divide by zero
print(Divide(4, 3))
