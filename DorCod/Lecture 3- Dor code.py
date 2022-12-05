#If statment

num = int(input("Enter a number:"))

if num % 39== 0:
    print(num,"is divisible by 39")
else:
    print(num, "is not divisible by 39")

#Else

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

if num1 > num2:
    print('num1 is bigger!')
else:
    print('num2 is bigger!')

#Corners

Corners=int(input("My hat has three corners:"))

if Corners==3:
    print("This is my hat!!!")
else:
    print("This is not my hat!!!")

#Elif

#Why worry?

Answer=input("Do you have a problem in life:")

if Answer=='Y':
    Answer = input("Can you do something about it:")
    if Answer=='Y':
        print("Than why worry?")
    elif Answer == 'N':
        print("Than why worry?")
    else:
        print("Not a valid answer")
elif Answer=='N':
    print("Than why worry?")
else:
    print("Not a valid answer")

#Price

price = int(input('Please enter a smart-phone price:'))

if price < 500:
    print('Very cheap!')
elif price < 2000:
    print('cheap')
elif price < 3000:
    print('medium')
elif price < 5000:
    print('Expensive')
else:
    print('Very expensive!')

#Hands on-if statmants

#---1---Create a Python script that accept a number a print if the number is odd or even
#---2--- Create a Python script to set if 3 numbers are a pythagoras triplet or not
#---3---Create a Python script that recive 2 numbers and an operation(+,-,*,/,**), and
#return the score

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

n = int(input("Enter a number:"))

if n % 2!=0:
    print("n is odd")
else:
    print("n is even")

#---2---

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))

if a^2+b^2==c^2:
    print("It's a pythagoras triplet")
elif c^2+b^2==a^2:
    print("It's a pythagoras triplet")
elif c^2 + a^2 == b^2:
    print("It's a pythagoras triplet")
else:
    print("It's not a pythagoras triplet")

#---3---

n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
print("+ for addition")
print("- for Subtraction")
print("* for multiplication")
print("\ for division")
print("** for power")
ch = input("Enter the choice:")

if ch=='+':
    ans = n1 + n2
elif ch == '-':
    ans = n1 - n2
elif ch == '*':
    ans = n1 * n2
elif ch == '/':
    ans = n1 / n2
elif ch == '**':
    ans = n1 ** n2
else:
    print("Invalid choice")

print("The answer is:",ans)

#For loop

name = 'Klay'

for letter in name:
    print ("Give me", letter)

print ("What did we get?", name)

#Range

x= range(0,len(name)+1)

for n in x:
    print(n)

x=range(10)

for n in x:
    print(n)

x = range(0,10,2)

for n in x:
    print(n)

x = range(10,0,-2)

for n in x:
    print(n)

x = range(1,101)

for n in x:
    print(n)

#Hands on-for loop

#---1---Create a Python script that print only the even numbers in the tuple
#---2---Create a Python script that divied list of positive and negative intagers to 2 list
#---3---Create a Python script  to accept a number from a user and calculate
# the sum of all numbers from 1 to a given number
#---4---Create a Python script to give only the uniqe numbers form a list

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

my_tup = (10,21,102,30,100,41,50,17)

for i in my_tup:
    if i%2==0:
        print(i)

#---2---

list = [22, -5, -6, 45, 93, -44]

Pos = []
Neg = []

for i in range(len(list)):
    if list[i] < 0:
        Neg.append(list[i])
    else:
        Pos.append(list[i])

print(Pos, Neg)

#---3---

s = 0
n = int(input("Enter number:"))

for i in range(1, n + 1, 1):
    s += i
print("Sum is: ", s)

#---4---

nums = [1, 8, 6, 4, 8, 5, 9, 6, 2, 3, 1, 5, 9, 7, 5, 2, 6, 5, 1, 8, 9, 2, 2, 1]

new_num = []

for i in nums:
    if i not in new_num:
        new_num.append(i)
        #new_num.sort()
print(new_num)

#While loops

number = 1

while number <11:
    print(number)
    number += 1

#Factorial

n = int(input())

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i +=1
print (n, "! = ", fact)

#infite loop

i = 1
while i < 4:
    print (i)
    break

#Hands On-while loops

#---1---Create a Python script to give the modulo of 2 numbers--
#---2---Create a Python script to play 7 Boom---
#---3---Create a Python script to calculate the deposit in 10 years
#deposit*(1+rate)

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

numb1= int(input("Enter a number:"))
numb2= int(input("Enter a number:"))

while(numb1>=numb2):
    print(numb1%numb2)
    break

#---2---

#A

a = 1

while a <= 100:
    if a % 7 == 0:
        print("Booom")
    if a % 7 != 0:
        print(a)
    a = a + 1

#B

nums = range(1, 100)

while True:

    for i in nums:
        if i % 7 == 0:
            print("Boom")
        else:
            print(i)
    break

#Advance

number = 1

while number <= 100:
    if number>9:
        str_number=str(number)
        if number%7 == 0 or str_number[0]=='7' or str_number[1]=='7':
            print('Boom!')
        else:
            print(number)
        number += 1
    else:
        str_number = str(number)
        if number % 7 == 0 or str_number[0]=='7' :
            print('Boom!')
        else:
            print(number)
        number += 1

def Boom(number,boom):

    while number <= 100:
        if number > 9:
            str_number = str(number)
            if number % boom == 0 or str_number[0] == str(boom) or str_number[1] == str(boom):
                print('Boom!')
            else:
                print(number)
            number += 1
        else:
            str_number = str(number)
            if number % boom == 0 or str_number[0] == str(boom):
                print('Boom!')
            else:
                print(number)
            number += 1

Boom(1,4)

#---3---

year = 2022
deposit = 2000
rate = 0.02
period = 10

#round(deposit * (1 + rate), 2)

counter = year

while counter <= year + period:
    deposit = round(deposit * (1 + rate), 2)
    print(str(counter) + ': ' + str(deposit))
    counter += 1