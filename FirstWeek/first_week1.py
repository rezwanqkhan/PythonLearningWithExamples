# first week
#Happy to see you here, happy coding!


# comments start with # in python
print("hello World")

""" this command written for
 more than one line in python"""

""" there is no need to declare variable in python
and the variables names are case sensitive which is variable A is different than B"""

# Arithmatic operators
x = 45
y = 20

print(x + y)  # addition
print(x - y)  # subtraction
print(x * y)  # multi...
print(x / y)  # division
print(x % y)  # models
print(x ** y)  # exponentiation(us alma)
print(x // y)  # floor division(how many times divided)

x += 3
x -= 3
x %= 3  # or x%3
print(x)

z = 8
z ^= 3
""" it applies the XOR operation with 3 using the ^= operator to 
the current value of z. XOR operation returns 1 
if the corresponding bits of the two operands are different, otherwise, 
it returns 0.
first :  8   = 1000
         3   = 0011
         
         When XOR operation is applied:
             1000
         XOR 0011
         --------
             1011
       As a result, the value of z becomes 11.
"""
print(z)

x = 10
x >>= 3
"""
This Python code first assigns the value 10 to a variable x.
 Then, it applies the right shift bitwise operation with a 
 shift of 3 to the current value of x using the >>= operator.
 
 In this case, shifting 10 (which in binary is 1010) three positions to
  the right yields 0001
  So, after the right shift operation, the value of x becomes 1"""
print(x)

x = 3
x &= 4
"""This Python code first assigns the value 3 to a variable x.
 Then, it applies the bitwise AND operation with 4 to the current 
 value of x using the &= operator.
 
 3   = 0011
 4   = 0100
 Performing the bitwise AND operation:
      0011
AND  0100
-----------
     0000
As a result, the value of x becomes 0.
"""
print(x)

x = 3
y = 3
print(x is y)  # true
# List
# List are created using square brackets
mylist = ["apple", "banana", "cherry"]
print(mylist[0])
mylist = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
print(mylist[-1])  # print the last element of list
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(mylist[2:5])  # Range :   bring from two till 5( 5 is not included)

print(mylist[:2])  # from zero until 2

print((mylist[4:]))  # bring from 4 till last element of list

print(mylist[-3:-1])  # bring from -3 until -1 which is the last element
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist[1] = "grap"  # second items which is banana changed to grap
print(mylist)
# change in range
mylist[1:3] = ["grap", "pear"]
mylist.append("banana")  # append() add the item in the lat element of list
print(mylist)

mylist.insert(1, "orange")  # insert the orange in the 1st index of the list
print(mylist)

addlist = ["mango", "pineapple", "cherry"]
mylist.extend(addlist)  # extend or add the addlist to mylist from the last
print(mylist)

mylist.remove("grap")  # remove grap from list
print(mylist)

mylist.pop(1)  # remove the 1st index item from list
print(mylist)

mylist.pop()  # if we do not add any index it will remove the last item of array
print(mylist)

del mylist[0]  # it is also delete the first item of array
print(mylist)

mylist.clear()  # delete all items of the array but mylist still available but empty

print("the elements of the list is cleared", mylist)

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

for x in mylist:  # print all items of my list in for loop
    print(x)
print(" ")
for x in range(len(mylist)):  # using the length of the in for loop it is also print all the items of the list
    print(mylist[x])
print(" ")
[print(x) for x in mylist]  # this is also print all item of the list shortest way

print("conditional")
mylist = [x for x in mylist if x != "apple"]  # print all without the apple
print(mylist)

print("sort the items")
mylist.sort()  # sorted by the alphabet
print(mylist)

print(" sort in revers")
mylist.sort(reverse=True)

print(mylist)

print("copy the list")
newlist = mylist.copy()
print(newlist)

print("join to list")
joinedlist = mylist + newlist
print(joinedlist)

# tuples are used to store multiple items in a single variable
# tuples are unchangeable
print("tuples")
mytuples = ("ahmet", "apple", "cherry", "orange", "apple1")
print(mytuples)
print("tuples items can be any types of data")
tuples1 = ("apple", 34, True, 34.5)
print(tuples1)
print("accessing the items in tuples is same with the list")
print(mytuples[0])  # ahmet
print("from negative items")
print(mytuples[-1])  # last item which is apple1
print("Range is also same with the list in tuples")
print(mytuples[1:3])
print("for changing the  items in tuples we have to convert it to list then to tuple")
newtupls = list(mytuples)
newtupls[1] = "orange"
mytuples = tuple(newtupls)

print(mytuples)

print("for adding items in tuples we have to do same way with changing tuple")
newtuples = list(mytuples)
newtuples.append("kiwi")  # add it to the last item of the list
mytuples = tuple(newtuples)
print(mytuples)
print("we can add tuples to other tuples")
newtupll = ("pear",)
mytuples += newtupll
print(mytuples)

print("we can remove items from tuple then we use the same way as adding in tuples")
newtuplll = list(mytuples)
newtuplll.remove("ahmet")
mytuples = tuple(newtuplll)
print(mytuples)
""" when we create a tuple we normally assign value to it, it is called packing a tuple
 in python we are also allowed to extract the values back to variables, this is calling unpacking"""
mytuplee = ("ahmet", "mahmud", "amir khan")
(first, second, third) = mytuplee
print(third)  # output is amir khan
print(first)  # ahmet

print("loops in tuple ")

for x in mytuples:
    print(x)

print("loops through the index numbers")

for x in range(len(mytuples)):
    print(mytuples[x])

print("joining two tuples")
firsttuple = ("apple", "orange", "kiwi")
secondtuple = ("ahmad", "rafi", "rashid khan")
alltuples = firsttuple + secondtuple
print(alltuples)
print("multiply tuples")
multipliedtuple = mytuples * 4
print(multipliedtuple)
print(multipliedtuple.count("orange"))  # how many orange are available in the tuple

# dictionaries are used to stor data value in key:value pairs
print("dictionary")
mydict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(mydict)
print(mydict["brand"])  # output is Ford
print("changing the item of the dict by using its key")
mydict["year"] = 2024
print(mydict)
print("we can also add into dict by key and its value")
mydict["color"] = "red"
print(mydict)

print("removing item from dict")
mydict.pop("model")  # model key with its value deleted
print(mydict)
print("using del  for removing item")
del mydict["color"]
print(mydict)
mydict["color"] = "red"

for x in mydict:
    print(mydict[x])

print("using values method")
for x in mydict.values():
    print(x)

print("copy a dict")  # we can not use dict1 = dict2
newdict = mydict.copy()
print(newdict)

print("conditions in python")
a = 10
b = 20

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

a = 10
b = 10

if b > a:
    print("b is greater than a")

elif a == b:
    print("a equal to b ")
a = 10
b = 20

print("shortest ways")
if a > b: print("a is grater than b ")

print(a) if a > b else print(b)

print("loops in python")

i = 1
while i < 6:
    print(i)
    i += 1

print("stop the loop when the i equal to 3")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("print all without 3")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("we use the else when to inform that the condition is not longer true")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print(" i is no longer greater than 6")

fruits = ["apple", "banana", "kiwi", "pear"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("for with range function")
"""for with range function, range() return a sequence number from zero and
 increments as default 1 and end by specific number"""
for x in range(10):  # print from 0 till 9
    print(x)

for x in range(5, 10):  # print from 5 till 9
    print(x)

for x in range(1, 10, 3):  # start from 1 increment 3 by 3 until 9  output: 1 4 7
    print(x)


