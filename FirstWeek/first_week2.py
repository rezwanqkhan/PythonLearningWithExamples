# first week 2nd part


print("functions in python")

# in python a function is defined using def keyword

def my_function():
    print("hello from a function")


# we can also add argument in functions
def my_Function(name):
    print("your name is " + name)


my_Function("rashid khan")  # calling function


# by adding * before argument it means the function will receive a tuple of arguments
def my_functionn(*name):
    print("your first name is " + name[0])  # print the first item of tuple


my_functionn("mustafa", "amir khan", "ramin")  # output is mustafa


# by adding ** before the arguments it means the function will receive a dictionary
def my_functionnn(**person):
    print("Last name is " + person["lastname"])


my_functionnn(firstname="x", lastname="y")


def my_functionnnn(country="brazil"):
    print("I am from " + country)


my_functionnnn()  # i am from brazil
my_functionnnn("cuba")  # i am from cuba


def my_functionnnnn(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_functionnnnn(fruits)  # calling the function that prints all item of the fruit list

print("use return to let a function to return a value")


def my_func(x):
    return x * 8


print(my_func(5))


def myfunction():  # if the func is empty then add pass for avoid the error
    pass


print("Lambda function")
"""A lambda func is a small anonymous func, ot can take any number of argument 
bu it can only have one expression( This will raise a SyntaxError
lambda x, y: x + y; x * y)

Lambda arguments: expression
"""
x = lambda a: a * 20
print(x(10))

x = lambda a, b, c: a * b * c - 4 - a  # output is 20
print(x(3, 3, 3))

print("Classes in python")


# to create a claas in python we use the class keyword
class MyClass:
    x = 5


# let's create an object from MyClass
p1 = MyClass
print(p1.x)

print("the __init__ funtion")
"""
In Python, the __init__ method is a special method
 used for initializing newly created objects. It's called a constructor method 
 because it initializes the object's attributes. When you create a new instance of a class, 
 Python automatically calls the __init__ method for that class."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)  # Output: 30

print("__str__  method in python")
"""The __str__ method in Python is another special method, 
also known as the "magic method" or "dunder method".
 It's used to define the string representation of an object. 
 When you use the str() function or print() function on an object, 
 Python internally calls its __str__ method to convert the object into a string."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f" Name : {self.name}, Age : {self.age}"


p1 = Person("Amir khan", 35)
print(p1)  # here we do not need to person1.name ...... cuz of __str__ method

"""object can also contain methods, 
Methods in object are function that belong to the object"""


class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def myfunct(self):
        print(f"Hello my name is {self.name}, I am {self.age} years old.")


p2 = Person("Rashid khan", 29)
p2.myfunct()  # output: Hello my name is Rashid khan, I am 29 years old.

# change the age
p2.age = 30
p2.myfunct()  # ................... 30

# delete object
del p2.age
print("inheritance in python")
"""Inheritance allows us to define a class that inherits 
all the methods and properties from another class 
"""


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printfullname(self):
        print(f"My full name is {self.firstname + ' ' + self.lastname}")


pp1 = Person("Amir", "Khan")
pp1.printfullname()


# let's inherit from Person class
class Student(Person):
    pass  # we have to use pass bends this class has not any properties and method yet


std1 = Student("Ahmet", "Kaya")
std1.printfullname()

print("local scope")


# a variable inside the function can be used only insife the function
def myfunc():
    x = 300
    print(x)


myfunc()

print("Function inside function it is possible in python")


def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()  # output is 300

print("Global variable")

x = 300


def myfunc():
    print(x)


myfunc()
print(x)

print("Naming variables")
""" if a variable inside and outside of function has different values
 in this case python tread them as two separate variables"""
x = 300


def myfunc():
    x = 200
    print(x)


myfunc()  # 200
print(x)  # 300

print("models in python")

import firstweekModel as fwm

fwm.greeting("Ahmet")  # comes from firstweekModel.py
a = fwm.person1["country"]
print(a)  # comes from firstweekModel.py

from firstweekModel import person1  # we can call specific part of models
print(person1["age"])  # 32

# there are another modules we can import
import platform

x = platform.system()
print(x)  # windows
y = platform.machine()
print(y)
z = platform.node()
print(z)

# mylist = ["python", "hub"]
# for i in mylist:
#     mylist.append(i.upper())   #infiniti loop
#     print(i)
# print(mylist)
