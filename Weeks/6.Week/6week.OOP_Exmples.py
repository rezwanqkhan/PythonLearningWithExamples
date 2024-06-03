
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


"""Example 8. Student scenario
Create Student class. Attributes are firstname, lastname, skills. Create student_info, add_skill functions.
student_info gives info of student and add_skill add the skill to student skills.
"""

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
"""Example 8. Employee scenario
Create Employee class. Attributes are name, salary. Create show function that gives info of employee
and salary salary will be private variable.
"""

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def showinfo(self):
        print("Name: ", self.name)
        print("Salary: ", self.__salary)


Person1 = Employee("John", "8000$")
Person1.showinfo()
