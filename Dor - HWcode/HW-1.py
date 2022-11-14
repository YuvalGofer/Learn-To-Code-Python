#Home work

#---1--- create a Python script which accepts the user's first and last name
# and print them in reverse order with a space between them.
#---2--- create a Python script which accepts an integer (n)
# and computes the value of n+nn+nnn.
#---3---create a Python script which get a string from a given string
# where all occurrences of its first char have been changed to '$',
# except the first char itself.
#---4---create a Python script which single string from two given strings
# ,separated by a space and swap the first two characters of each string

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

str="Dor Shani"

index=str.index(" ")

print("Hallo"+' '+str[index+1:]+' '+str[0:index])

#----------------------------

str="Dor Shani"

l=str.split(" ")

print("Hallo"+' '+l[1]+' '+l[0])

#---2---

a = int(input("Input an integer : "))

n1 = a
n2 = a*11
n3 = a*111

print(n1+n2+n3)

#-----------------------------------

N = input("Enter a number:")

Sum = int(N)+int(N+N)+int(N+N+N)

print(Sum)

#---3---

#A

str = "restart"
str_print = str[1:].replace('r', '$', 1)
print("r"+str_print)

#B

Rev_str=str[::-1]

print(Rev_str)

new_Rev_str=Rev_str.replace('r', '$', 1)

print(new_Rev_str)

new_str=new_Rev_str[::-1]

print(new_str)

#---4---

str1 = input("Enter first string:")
str2 = input("Enter second string:")
N1 = str1.replace(str1[:2], str2[:2])
N2 = str2.replace(str2[:2], str1[:2])
print(N1 +" "+N2)

#-----------------------------------

a=input("Input a string : ")
b=input("Input b string : ")

new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]

print(new_a,new_b)