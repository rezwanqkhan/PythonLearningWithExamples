# hey welcome to second week lesson
# HAPPY  CODDING


A = [100]
B = A
C = A.copy()
# the id function shows the address of data in memory
print(id(A))
print(id(B))
print(id(C))

# type fuc determine which type of data type is it
A = 100
print(type(A))


# How to we can count the instance with class public attributes
class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


# the below code actually calls the __init___ func
x = C()
print("number of instance: " + str(C.counter))  # 1
y = C()
print("number of instance: " + str(C.counter))  # 2
# the below code actually calls the __del___ func
del x
print("number of instance: " + str(C.counter))  # 1
del y
print("number of instance: " + str(C.counter))  # 0


## for makin private of an atrribute
# for making private an attribute we have to use double underscore(like __counter)
# for making access to the private attribute we use instance methods
class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def RobotInstance(self):  # class method to access to the private attribute
        return Robot.__counter


x = Robot()
print(x.RobotInstance())  # accessing by the instance method  1
y = Robot()
print((y.RobotInstance()))  # 2

print(Robot.RobotInstance(x))  # 2  just call the value

# if we wanna access directly to the method we add @staticmethod
print("@staticmethod")


class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstance():  # class method to access to the private attribute
        return Robot.__counter


print(Robot.RobotInstance())  # it returns the value of the __counter   0
x = Robot()
print(x.RobotInstance())  # 1
y = Robot()
print(y.RobotInstance())
print(Robot.RobotInstance())  # 2

# important
""" instance method get self in first argument @staticmethod doesn't get any implicit first argument  and @classmethod 
get cls in first argument """

"""# the main different between staticmethod and @classmethod is in the class method 
we can use method of its class or create a new instance but in the @static method it is impossible
"""


class MyClass:
    class_variable = 0

    @classmethod
    def class_method(cls):
        """
        This is a class method.
        It can access and modify class-level variables and methods.
        It automatically receives a reference to the class (cls) as the first parameter.
        """
        cls.class_variable += 1  # Accessing and modifying class-level variable
        return cls.class_variable

    @staticmethod
    def static_method():
        """
        This is a static method.
        It cannot access or modify class-level variables or methods directly.
        It does not receive a reference to the class or its instances as parameters.
        """
        return "This is a static method"


# Calling the class method
print(MyClass.class_method())  # Output: 1
print(MyClass.class_method())  # Output: 2

# Calling the static method
print(MyClass.static_method())  # Output: "This is a static method"


# def gcd(c, d):                 5 | 20, 15
#     while d != 0:                | 4, 3
#         c, d = d, c % d
#     return c
# print(gcd(20,15))   # 5
class Fraction(object):
    def __init__(self, n, d):
        self.numrator, self.demnumrator = Fraction.reduce(n, d)

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b  # a equal to b then b equal to a%b(mood)
        return a

    @classmethod
    def reduce(cls, n1, n2):  # cls is used for using the classmethode
        g = cls.gcd(n1, n2)  # here we could access to  the class method by @classmethod
        return (n1 // g, n2 // g)

    # we had used the str function to return the value of the object
    def __str__(self):
        return str(self.numrator) + '/' + str(self.demnumrator)


x = Fraction(20, 15)
print(x)  # 4/3
print(x.numrator, x.demnumrator)  # 4 3


# getter and setter in python
class P:

    def __init__(self, x):
        self.__x = None
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p1 = P(1001)  # first run the __init__ and __init__ runs the set_x and return the value
print(p1.get_x())
p1.x = 1001  # does not detect this class
print(p1.x)  # 1001

# let's use the @ property and @x.setter
print("using @property and @x.setter")


class P:
    def __init__(self, x):
        # Initialize the instance with the provided value of x
        self.x = x

    @property
    def x(self):
        # Getter method for property x
        return self.__x

    # Setter method for property x
    @x.setter
    def x(self, x):
        # Check if the new value of x is less than 0
        if x < 0:
            # If so, set __x to 0
            self.__x = 0
        # Check if the new value of x is greater than 1000
        elif x > 1000:
            # If so, set __x to 1000
            self.__x = 1000
        else:
            # Otherwise, set __x to the new value of x
            self.__x = x


# Create an instance of class P with the initial value of 1001
p11 = P(1001)
# Print the value of the property x
print(p11.x)  # Output: 1000 (maximum value allowed)
# Attempt to set the value of x to 1001
p11.x = 1001
# Print the value of the property x again
print(p11.x)  # Output: 1000 (maximum value allowed)

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
