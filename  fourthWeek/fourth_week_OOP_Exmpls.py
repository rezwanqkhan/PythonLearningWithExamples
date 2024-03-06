

"""
1. Write a Python class to convert an integer to a Roman numeral.
"""
def int_to_roma(GivenNum):
    intList =[1000,900,500,400,100,90,50, 40, 10,9, 5 ,4, 1 ]
    Romasymb = ["M", "CM", "D", "CD", "C", "XC", "L","XL", "X", "IX",  "V", "IV", "I"]
    roma_num = ''

    i =0
    while GivenNum > 0:
         for x in range(GivenNum // intList[i]):
             roma_num += Romasymb[i]
             GivenNum -= intList[i]
         i+=1
    return  roma_num

print(int_to_roma(100))


"""
Example 2. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and
emp_department and methods like calculate_emp_salary, emp_assign_department, and
print_employee_details.
overtime = hours_worked – 50
Overtime amount = (overtime * (salary / 50))
Departments: Accounting, Sales, Operations, Research
Tasks:
Create 4 people according to Employee class.
Two person must be over 50 hours worked.
Two person must change their departments
"""

class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

    def calculate_salar(self, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
            self.salary = self.salary + (overtime * (self.salary / 50))
        else:
            self.salary = self.salary + (overtime * (self.salary / 50))

    def assign_depm(self, emp_deprtm):
        self.department = emp_deprtm

    def print_emp_detil(self):
        print('Name: ', self.name)
        print('ID: ', self.emp_id)
        print('Name: ', self.salary)
        print('Name: ', self.department)


John = Employee('John', 1, department='security', salary=7500)
John.calculate_salar(75)
John.assign_depm('software tester')
John.print_emp_detil()
print('\n')
Rose = Employee('Rose', 1, department='Manager', salary=7500)
Rose.calculate_salar(20)
Rose.assign_depm('CEO')
Rose.print_emp_detil()

"""Example 3. Write a Python class BankAccount with attributes like account_number, balance,
date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance"""
"""
● Create 3 bank accounts for customers
● Add amount 3000 to first customer account
● Withdraw 2000 from second customer account
● Add amount 1000 to third customer account
● Display all customers bank information"""


class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, balance):
        self.balance -= balance;

    def check_balance(self):
        return f"Customer Name: {self.customer_name}\nDate of Opening: {self.date_of_opening}\nAccount Number: {self.account_number}\nBalance: {self.balance}\n"


Ahmet = BankAccount(1, 10000, 2017, 'ahmet')
Watson = BankAccount(3, 110000, 2007, 'Watson')
Alex = BankAccount(4, 120000, 2015, 'Alex')

Ahmet.deposit(3000)
Watson.withdraw(2000)
Alex.deposit(1000)

print(f"FIRST Customer's details \n{Ahmet.check_balance()}")
print(f"SECOND Customer's details \n{Watson.check_balance()}")
print(f"THIRD Customer's details \n{Alex.check_balance()}")
