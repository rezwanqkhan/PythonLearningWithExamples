import time
import math


def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in ", func.__name__, end - begin)

    return inner


@calculate_time
def Factorial(num):
    time.sleep(0.1)
    print(math.factorial(num))


Factorial(100)


def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in ", func.__name__, end - begin)

    return inner


@calculate_time
def fibonacci(num):
    n1, n2 = 0, 1
    counter = 0
    next = 0
    print("Fibonacci Sequence: ")
    while counter < num:
        # print(next, )
        next = n1 + n2
        n1 = n2
        n2 = next
        counter += 1
    print("Finished: ", next)


print(fibonacci(10))

# we can use decorator as nested
"""Chaining Decorators
In simpler terms chaining decorators means decorating a function with multiple decorators."""


def decor1(func):
    def inner():
        print("inside decor1()")
        x = func()
        return x * x

    return inner


def decor2(func):
    def inner():
        x = func()
        print("inside decor2()")
        return 2 * x

    return inner


@decor1  # second
@decor2  # first
def num():
    # print("inside num()")
    return 10


@decor2
@decor1
def num2():
    return 10


print(num())  # 400
print(num2())  # 200


# Decorators with parameters is similar to normal decorators.

def decoretor(*args, **kwargs):
    print("inside decorator")

    def inner(func):
        print("inside inner function")
        print("I like", kwargs['like'])
        func()

    return inner


@decoretor(like="Python")
def my_function():
    print("Inside actual function")


"""
output:
inside decorator
inside inner function
I like Python
Inside actual function"""

"""Decorators with parameters is similar to normal decorators.
"""
print("decorator with parameters")


def decorator(x, y):
    def inner(func):
        def wrapper(*args, **kwargs):
            print("inside decorator")
            print("I like python")
            print("summation of values:", str(x + y))
            func(*args, **kwargs)  # my_func  executes here

        return wrapper

    return inner


def my_func(*args):
    print("inside my_func")
    for arg in args:
        print(arg)


decorator(10, 25)(my_func)('Hello', 'my', 'Python')
"""
output:
inside decorator
I like python
summation of values: 35
inside my_func
Hello
my
Python"""

"""super() in Python allows a subclass to call methods from its superclass, 
facilitating code reuse and extending functionality while maintaining the class hierarchy"""


class A:
    def greet(self):
        print("Hello from class A")


class B(A):
    def greet(self):
        super().greet()  # Calling the greet method of class A
        print("Hello from class B")


B = B()
B.greet()
"""
Hello from class A
Hello from class B"""

# Polymorphism: one method, multiple behaviors based on parameters.
print("\nPolymorphism")


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


def make_animal_speak(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()
cow = Cow()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
make_animal_speak(cow)  # Output: Moo!


# from lecture
class Shape:
    def area(self):
        # you can write pass
        pass
        # raise NotImplementedError("subclass most implement the 'area' method")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius


shapes = [Rectangle(5, 4), Circle(3)]

for shap in shapes:
    print(shap.area())

# for using abstract class we have to import from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

print("\n abstract base class")
"""Abstract Base Classes (ABCs): ABCs provide a way to define interfaces or contracts in Python.
 They allow you to define a set of methods that must be implemented by concrete subclasses. 
 ABCs cannot be instantiated directly; 
 they serve as templates or blueprints for other classes to inherit from. 
ABCs are used to enforce a contract or interface across multiple classes,"""


# Define an abstract base class (ABC) called Shape
class Shape(ABC):
    # Define an abstract method area() without implementation
    @abstractmethod
    def area(self):
        pass

    # Define another abstract method perimeter() without implementation
    @abstractmethod
    def perimeter(self):
        pass


# Define a concrete subclass Rectangle that inherits from Shape
class Rectangle(Shape):
    # Constructor to initialize width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the area() method for Rectangle
    def area(self):
        return self.width * self.height

    # Implement the perimeter() method for Rectangle
    def perimeter(self):
        return 2 * (self.width + self.height)


# Create an instance of Rectangle with width 5 and height 4
rect = Rectangle(5, 4)

# Call the area() and perimeter() methods of Rectangle
print("Area:", rect.area())  # Output: Area: 20
print("Perimeter:", rect.perimeter())  # Output: Perimeter: 18
