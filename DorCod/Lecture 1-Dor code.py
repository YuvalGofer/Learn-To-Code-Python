#First code

print("Hello World")

#integers

first_int = 2
second_int = 2

print(type(first_int))

print(first_int)
print(second_int)

second_int = 3

print(first_int)
print(second_int)

first_big_int = first_int*100
second_big_int = second_int*100

print(first_big_int)
print(second_big_int)

first_big_int = first_int**100
second_big_int = second_int**100

print(first_big_int)
print(second_big_int)

#float

first_float = 2.717
second_float = 2.717

print(type(first_float))

print (first_float)
print (second_float)

second_float = 3.14

print (first_float)
print (second_float)

first_big_float= first_float*100
second_big_float = second_float*100

print (first_big_float)
print (second_big_float)

first_big_float = first_float**100
second_big_float = second_float**100

print (first_big_float)
print (second_big_float)

#Strings

word1 ="Hello"
word2="World"

print(type(word1))

print(word1)
print(word2)

print(word1+word2)

print(word1+' '+word2)

print("Hello\n \nWorld")

print("hello world")
print("dgfsg")

#String slicing

str="We are learnnig Python!!!"

print(str)

print(str[3])

print(str[1:4])

print(str[1:])

print(str[-20])

print(str[-4:-2])

print(str[:-3])

print(str[-3:])

print(str[::-1])

print(str[::2])

#String functions

print(len(str))

print(str.upper())

print(str)

print(str.lower())

print(str)

print(str.index('e'))

print(str)

print(str.replace('a','e'))

print(str)

print(str.replace('a','e',1))

print(str.count('r'))

IP="Pink Floyd"

IP_Oct=IP.split()

print(IP_Oct[1])

#common mistake

word1="Hallo"
first_int=2

print(word1+first_int)

type(first_int)

first_int_str=first_int.__str__()

type(first_int_str)

print(word1+first_int_str)

#Input

str1=input("Enter a String:")
str2=input("Enter a String:")

x=int(input("Enter a Number:"))
y=int(input("Enter a Number:"))

print(str1+" "+str2)
print(x*y)

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
