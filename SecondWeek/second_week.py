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
