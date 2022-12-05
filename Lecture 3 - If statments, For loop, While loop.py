#If statments
#Exercise 1. Create a Python script that accept a number a print if the number is odd or even

num = int(input("Enter a number.."))
if num % 2 == 0:
    print("This number is even!")
else:
    print("The number is odd")

#Exercise 2. Create a Python script to set if 3 numbers are a pythagoras triplet or not
a = int(input("Enter a numnber"))
b = int(input("Enter a second numnber"))
c = int(input("Enter a third numnber"))
if a^2 + b^2 == c^2:
    print("It's a pythagoras triplet!!")
elif b^2 + c^2 == a^2:
    print("It's also a pythagoras triplet!!")
elif a^2 + c^2 == b^2:
    print("It's also a pythagoras triplet!!")
else:
    print("It's not a pythagoras triplet!")


#Exercise 3. Create a Python script that recive 2 numbers and an operation(+,-,*,/,**), and return the score
num1 = int(input("Enter a numnber"))
num2 = int(input("Enter a second numnber"))
operation = input("Choose an operation +, -, /, *, **")
ans = ''
if operation== "+":
    ans=num1 + num2
elif operation=="-":
    ans=num1 - num2
elif operation=="*":
        ans=num1 * num2
elif operation == "/":
        ans=num1 / num2
elif operation=="**":
    ans=num1 ^ num2
else:
    print("Invalid operation!")

print("The answer is:", ans)

#Exercise 4. Create a Python script that print only the even numbers in the tuple
my_tup = (10,21,102,30,100,41,50,17)
for n in my_tup:
    if n % 2 ==0:
        print(n)
    else:
        print('')
#Exercise 5. Create a Python script that divied list of positive and negative intagers to 2 list
list = [22, -5, -6, 45, 93, -44]

Pos = []
Neg = []

for x in list:
 if x <0:
   Neg.append(x)
 else:
     Pos.append(x)

print("Negative list:", Neg,','  "Positive list:", Pos)



#Exercise 6. Create a Python script  to accept a number from a user and calculate the sum of all numbers from 1 to a given number
number = int(input("Give a number from 1-5"))
summary = []
for x in range(1,number+1):
   if x in summary:
       continue
   summary.append(x)

print(summary)
print("Summary of numbers from 1 to", number, "is:",  sum(summary))

 #Exercise 7. Create a Python script to give only the unique numbers form a list
nums = [1, 8, 6, 4, 8, 5, 9, 6, 2, 3, 1, 5, 9, 7, 5, 2, 6, 5, 1, 8, 9, 2, 2, 1]
uniques = []
for x in nums:
    if x in uniques:
            continue
    uniques.append(x)

print(uniques)

#Factorial
n=int(input("...?"))
fact = 1
i = 1
while i<=n:
    fact = fact*i
    i += 1
    print(i)
print(n, "!=", fact)

#Factorial2
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        print(i)
        fact *=i
        print(fact)
    return fact

print("7!= ", factorial(7))

#Attention!! infinity loop
i=1
while i<4:
    # i +=1 or put break after print(...)
    print(i)
    #break

#While loop exercise
# 1.Create a python script to give thge modulo of 2 numbers
number1=int(input("1st number please"))
number2=int(input("2nd number please"))
while number1 > number2:
    print(number1%number2)
    break

#Exercise 2.Create a python script to play 7 boom
#Solution1
a=1
while a<=21:
    if a % 7 == 0 :
     print("Boom")
    if a % 7 != 0:
     print(a)
    a += 1
#Solution2
num = range(1,21)
while True:
    for a in num:
        if a % 7 ==0:
            print("Boom")
        else:
            print(a)
    break
#Function result for 7 boom
def Boom(start, boom):

  while start <= 21:
     if start % boom == 0:
        print("Boom")
     if start % boom != 0:
        print(start)
     start += 1

Boom(1, 4)


#Exercise 3. Create a python script to calculate the deposit in 10 years: deposit*(1+rate)
year = 2022
deposit = 2000
rate = 0.02
period = 10
counter = year
while counter <= year + period:
    deposit = round(deposit*(1+rate),3)
    print(str(counter), ': ', str(deposit))
    counter += 1

#Hands on
#Exe 1. Python func to check wether a number falls in a given range
def testRange(a,b,c):
    if a in range(b,c+1):
        print(a, "Is in the range!")
    else:
        print(a, "Is not in the range")

print(testRange(8, 1, 9))

#Exe 2. Python func that takes a number as a parameter and check if prime or not
def prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
     for x in range(2, n):
        if (n % x==0):
              return False
        return True

print(prime(20))

#Exe 3. Python func to reverse a string
def testString(str):
    return str[::-1]

print(testString("Yuval"))

#Solution2 for exe 3.
def testReverseString(str):
    str2=''
    index=len(str)
    while index > 0:
        str2 += str[index-1]
        # print(str2)
        index=index-1
        # print(index)
    return  str2

print(testReverseString("Yuval"))

