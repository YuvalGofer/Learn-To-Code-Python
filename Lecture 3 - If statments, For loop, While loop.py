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

#HW
#Question
#1.What is the fifteenth letter of the alphabet?
#2.What is the code for the twenty third letter of the alphabet?
#3.What is the fourth letter of the code for the eighth letter of the alphabet?
Alphabet =  [["A", "Alfa"],
             ["B", "Bravo"],
             ["C", "Charlie"],
             ["D", "Delta"],
             ["E","Echo"],
             ["F", "Foxtrot"],
             ["G", "Golf"],
             ["H", "Hotel"],
             ["I", "India"],
             ["J", "Juliett"],
             ["K", "Kilo"],
             ["L", "Lima"],
             ["M", "Mike"],
             ["N", "November"],
             ["O", "Oscar"],
             ["P", "Papa"],
             ["Q", "Quebe"],
             ["R", "Romeo"],
             ["S", "Sierra"],
             ["T", "Tango"],
             ["U", "Uniform"],
             ["V", "Victor"],
             ["W", "Whiskey"],
             ["X", "X ray"],
             ["Y", "Yankee"],
             ["Z", "Zulu"]]
# 1. 15th letter is: O, Oscar
print(Alphabet[14][0])
#2. Code for the twenty third letter of the alphabet is: Whiskey
print(Alphabet[22][1])
#3. 4th letter of the code for the eighth letter of the alphabet is: e
print(Alphabet[7][1][3])

#Question 4. Create a Python script that to Convert a given tuple of positive integers into an integer
nums=(1,2,3)
combine = nums[0]*100+nums[1]*10+nums[2]
print(combine)

#Question 5. Create a Python script that change the first element in a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[0]="kiwi"
x=tuple(y)
print(x)

#Question 6. Create a Python script that combine values in python list of dictioneries.
#Results1
item_list = [{'item': 'item 1 ', 'amount': 400 }, {'item': 'item 2 ', 'amount': 300}]
items = {}
item_1={item_list[0]['item']:item_list[0]['amount']}
item_2={item_list[1]['item']:item_list[1]['amount']}
items.update(item_1)
items.update(item_2)
print(items)
#Results2
result={}
first_item=list(item_list[0].values())
second_list=list(item_list[1].values())
result.update({first_item[0]: first_item[1]})
result.update({second_list[0]:second_list[1]})
print(result)

#Factorial
n=int(input("...?"))
fact = 1
i = 1
while i<=n:
    fact = fact*i
    i += 1
    print(i)
print(n, "!=", fact)

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
#Function result
def Boom(start, boom):

  while start <= 21:
     if start % boom == 0:
        print("Boom")
     if start % boom != 0:
        print(start)
     start += 1

Boom(1, 3)

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