import string

from Tools.demo.beer import n

#First code - string

print("Hello World")
firstName = "Yuval"
secondName = "Gofer"

print(type(firstName))
print("Hi, \nyour full name is:", firstName+ " " +secondName)



#Integers
first_int = 2
second_int = 3

print(type(first_int))
print(second_int)

firstBigInt = first_int**2
secondBigInt = second_int**2

print(firstBigInt)
print(secondBigInt)

#String slicing
numbersOrder = "1234567"
print(numbersOrder[::-1])

nameSlicing = "Hi there!"
print(nameSlicing.replace("H", "?"))
print(nameSlicing.index("r"))

word1 = "World"
word2 = 2
wordFix = word2.__str__()
print(word1+ " " +wordFix)

#Inputs
firstName=input("Enter your first name..")
lastName=input("Enter your last name..")
print("Hello", firstName+ " " +lastName)

firstNumber = int(input("Enter a number.."))
secondNumber = int(input("Enter a second number.."))
print(firstNumber*secondNumber)

#Booleans
5 == 5.0

6 != 2*3

-2 >= 1

3 <= 3

a=5
b=3

a<b

#Logical Operators

x=True
y=False
z=True

print(x and y)

print(x and z)

print(x)

print(x or y)

print(not y)

str1 = input("Enter your name")
int1 = int(input("Enter your year born"))
age = 2022 - int1
age_print = age.__str__()
print("hello "+str1+" your age is: "+age_print)
