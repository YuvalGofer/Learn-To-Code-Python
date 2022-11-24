#HW-4

#---1---Create a Python script to create and print a list where the values are square of
# numbers between 1 and n (both included).
#---2---Create a Python script to find all keys in the provided dictionary that have the given value.
#---3---Create a Python script to calculate the value of the following expression by using lambda function.
#---4---Create a Python script to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result


#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

#Exc-1

def input_in_squere(number):
    list=[]
    while(number>0):
      list.append(number**2)
      number=number-1
    return list[::-1]

print(input_in_squere(5))

#Exc-2

n=int(input("Enter a number: "))

def printValues(n):
    l = []
    for i in range(1,n+1):
        l.append(i ** 2)
    print(l)

printValues(n)

#---2---

def test(dict, val):

    Keys=[]
    for key, value in dict.items():
        if value == val:
            Keys.append(key)
    return Keys

students = {'Theodore': 19,'Roxanne': 20,'Mathew': 21,'Betty': 20}

print(test(students, 22))

#---3---

print("Please enter the values of x, y and z")
x = int(input())
y = int(input())
z = int(input())

expr = lambda x, y, z: (x * 10) + (y / 2) * z

print(expr(x, y, z))

#---4---

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

r = lambda x, y : x * y

print(r(a, b))










