# Example 4. Write a Python code with functions multiplication, addition that performs arithmetics
# operations. Define a function calculation using created functions as a decorator. calculation function use
# one parameter and calculate using multiplication and addition, respectively.
# calculation(3)
# Inside the calculation function: 3
# Inside the multiplication function: 3
# Inside the addition function: 9
# 18

def multiplication(func):
    def innerfunction(*args, **kwargs):
        num = func(*args, **kwargs)
        print("inside the multiplication function", num)
        return num * num

    return innerfunction


def addition(func):
    def innerfunction(*args, **kwargs):
        num = func(*args, **kwargs)
        print("Inside the addition function", num)
        return num + num

    return innerfunction


@addition
@multiplication  # firstly execute
def calculation(x):
    print("inside the calculation function", x)
    return x


calculation(3)


# Example 5. Write a RationalNumber class with functions mul, add, sub, truediv that performs
# arithmetics operations for rational numbers.
# a = RationalNumber(I, 2)
# b = RationalNumber(1, 3)
# a + b
# 5/6
# a-b
# 1/6
# a * b
# 1/6
# a/b
# 3/2


class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __mul__(self, other):
        if isinstance(other, RationalNumber):
            return RationalNumber(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            return RationalNumber(self.numerator * other, self.denominator)

    def __add__(self, other):
        if isinstance(other, RationalNumber):
            return RationalNumber(self.numerator * other.denominator + other.numerator * self.denominator,
                                  self.denominator * other.denominator)
        else:
            return RationalNumber(self.numerator + other * self.denominator, self.denominator)

    def __sub__(self, other):
        if isinstance(other, RationalNumber):
            return RationalNumber(self.numerator * other.denominator - other.numerator * self.denominator,
                                  self.denominator * other.denominator)
        else:
            return RationalNumber(self.numerator - other * self.denominator, self.denominator)

    def __truediv__(self, other):
        if isinstance(other, RationalNumber):
            return RationalNumber(self.numerator * other.denominator, self.denominator * other.numerator)
        else:
            return RationalNumber(self.numerator, self.denominator * other)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# Example usage
a = RationalNumber(1, 2)
b = RationalNumber(1, 3)

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)

# Example 6. Collatz Problem: Start with a number n > 1. Find the number of steps it takes to reach one
# using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add I.
#
# def CollatzProblem(num):
#     steps = 0
#     while num > 1:
#         print(num)  # Print the current number
#         if num % 2 == 0:
#             num = num / 2
#         else:
#             num = (num * 3) + 1
#         steps += 1
#     print(num)  # Print the final number (which is 1)
#     return steps
#
#
# try:
#     start_number = int(input("Enter a number greater than 1: "))
#     if start_number <= 1:
#         raise ValueError("Input must be greater than 1")
#     steps_taken = CollatzProblem(start_number)
#     print("Number of steps taken to reach 1 starting from", start_number, ":", steps_taken)
# except ValueError as ve:
#     print("Invalid input:", ve)

"""
Example 7. Caesar cipher
The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding
replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key = 2 encrypts
"HI" to "JK", but key=20 encrypts "HI" to "BC".
(Note: ASCII code starts from A=65, chr() is to get character from ASCII table, ord() is to get ASCII value
of character. English alphabet has 26 letters).
Encrypt the text="KARATAY" using key=4
text = "KARATAY"
key = 4
print ("Text : " + text)
print ("Shift : " + str(key))
print ("Cipher: " + encrypt(text,key))"""


def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # print(char)
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text


text = "KARATAY"
key = 1  # LBSBUBZ

print("Text : " + text)
print("Shift : " + str(key))
print("Cipher: " + encrypt(text, key))





class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.skills = []

    def studentinfo(self):
        print("Student Name:", self.firstname)
        print("Student Last Name:", self.lastname)
        print(self.skills)

    def Addskills(self, skill):
      self.skills.append(skill)


A = Student("john", "Root")
A.Addskills("C")
print(A.studentinfo())

print("\nSalary Example")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def showinfo(self):
        print("Name: ", self.name)
        print("Salary: ", self.__salary)


Person1 = Employee("John", "8000$")
Person1.showinfo()
