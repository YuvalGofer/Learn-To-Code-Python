#---String---

my_pi=3.141592653589793
print(my_pi[10])

my_pi=str(my_pi)
print(my_pi[1])

#isdigit, isalpha

s=input()

s=s.split()

w=input()

count=0
for l in s:
    if l==w:
        count+=1
print(count)

s ="Python2022#"
d=l=0

for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        print(c,"Not a Digit nor a Letter")

print("Letters", l)
print("Digits", d)

#List

list1=[1,2,3,4,5,6]

list2=[7,8,4,32,6,2]

for i in list1:
    if i<2 or i>4:
        print(i)

for i in list1:
    if i>2 and i<5:
        print(i)

for i in list1:
    if i not in list2:
        print(i)

#---Hans on---

#---1---Create a Python script that prints each item and its corresponding type from the following list
#---2---Create a Python script that string from a given string where all occurrences of its first char
# have been changed to'$', except the first char itself

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

datalist = [1452, 11.23, 1+2j, True, (0, -1), [5, 12],
{"class":'V', "section":'A'}]

for item in datalist:
   print ("Type of ",item, " is ", type(item))

#---2---

#---index---

string = 'alphabat'

pos = string.index('a', string.index('a') + 1)
string = string[:pos] + '$' + string[pos + 1:]

print(string)

str1 = input("Enter a string")
word1 = str1[0]

for i in range(1,len(str1)):
    if str1[0] == str1[i]:
        str1[i] = "$"
print(str1)


#---while loop---

statement = 'laphabat'
counter = 1

while counter<2:
    for i in statement:
        if i == "a":
            counter = counter + 1
        first_half = statement[0:counter]
        second_half = statement[counter::]
print(first_half + second_half.replace('a','$'))


sum=0

while sum<300:
    sum+=5
    print(sum)
print(sum)

sum=0

n=int(input())

for i in range(0,300,n):
    sum += n
    print(sum)
print(sum)

#Hands on-Lecture 1

#---1---Create a script to get a number and check if the number bigger then 100 and divided by 3
# and a script to get a number and check if the number bigger then 100 or divided by 3
#---2---Create a script to print the following number pattern using a loop.
#---3---Create a script will get numbers from user until users enters 0.
# Program will print how many tried the user made

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

num = int(input('Please enter a number:'))

if num > 100 and num % 3 == 0:
    print('Yes')
else:
    print('No')

num = int(input('Please enter a number:'))

if num > 100 or num % 3 == 0:
    print('Yes')
else:
    print('No')

# -- Range check --#

if num > 100 and num < 300:
    print('Yes!')

#---2---

row = int(input('Please enter a number:'))

for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")

#---3---

numCount = 0
password=int(input('Please enter a password:'))

print('Please enter a number (print(0 to exit)')
number = int(input('Please check the password:'))

while number != 0:
    if number==password:
        print("Shoshmi open")
        break
    else:
        numCount += 1
        print('Please enter another number (0 to exit)')
        number = int(input('Please enter a password:'))

print('You have tried', numCount,'times')

#Hands on-Lecture 2

#---1---Create a script to an yearly based on montjly salary, if the user
#worked lass then 12 months' the program will stop
#---2---Define a function to check if a number is a prime or not
#---3---Create a Python script to convert a given list of lists to a dictionary with a roman letters
#and a name
#---4---Create a Python function to recive a first name, last name and an email domain(
#gmail.com, hitmail.com etc. and create a maul accounts from the 3 first letters form the
#first name(lower case), 3 first letters form the last name(lower case) and from the email domain

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

total = 0

for i in range(1, 13):
    print('Please enter your salary for month ', i)
    salary = int(input())
    if salary == 0:
        break
    total = total + salary

    print('This year you earned a total of: ', total)
    if i < 12:
        print('You worked only', i - 1, 'months')

#---2---

def prime_check(num):
    for n in range(2, num):
        if num % n == 0:
            return 'Not Prime!'
    return 'Prime Number!'

n = int(input('Please enter a number:'))

print(prime_check(n))

#---3---

def test(lst):
    Dict_list = {}
    for x,y,z in lst:
        Dict_list[x]=z
    return Dict_list

students = [['Jean Castro',1, 'V'], ['Lula Powell',2,  'V'],
            ['Brian Howell',3,  'VI'], ['Lynne Foster',4,  'VI'],
            ['Zachary Simon',5,  'VII']]

print(test(students))

#---4---

def gen_email(f_name,l_name,domain):

    return f_name[0:2].lower() + l_name[0:2].lower() + '@' + domain.lower()

print(gen_email('Dor','Shani','gmail.com'))

#Hands on-Lecture 3+4

#---1---Create a python function to recive the Price of a lottery card
# the prize, the number of Balls and the number of Balls Chosen

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

def lottery(Price,Money,Balls_Number,Balls_Chosen):

    def Prob(Balls_Number,Balls_Chosen):

        Probs=[]
        for i in range(Balls_Number-Balls_Chosen+1,Balls_Number+1):
            prob=1/i
            Probs.append(prob)
            totalSum = 1
            for number in Probs:
                totalSum *= number
            return totalSum

    Prob=Prob(Balls_Number,Balls_Chosen)
    if Price*Prob>Money:
        return "Take the chance"
    else:
        return "Not worth it"

print(lottery(20000000,5,37,6))

Probs=[]
n=int(input("Enter number of Chosen Balls"))
for i in range(38-n, 38):
    prob = 1 / i
    Probs.append(prob)
    print(Probs)
    totalSum = 1
    for number in Probs:
        totalSum *= number
print(totalSum)


#Lambada

Converter = lambda x : x*2 if x < 10 else (x*3 if x < 20 else x)

print(Converter(3))
print(Converter(12))
print(Converter(33))

#Strings

#---3---Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)

#While loop

#---1---Create a Python script to ask if the user wants to continue to add numbers to a list.
# If not, print the numbers and the sum of them

Numbers = []
testAnswer = input('Press y if you want to enter more numbers: ')

while testAnswer == 'y':
    num = int(input('Next number: '))
    Numbers.append(num)
    testAnswer = input('Press y if you want to enter more numbers:  ')

print('Your Numbers were:',Numbers,"The sum of you Numbers are:",sum(Numbers))

#dictionaries

#---1---Create a Python script to check whether a given key already exists in a dictionary.

x=int(input("Enter a number:"))

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

if x in d:
    print('Key is present in the dictionary')
else:
    print('Key is not present in the dictionary')

#---2---Create a Python script to find the key of the maximum value and minimum value in a dictionary.

def test(d):
  return max(d, key = d.get), min(d, key = d.get)

students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 18
}

#If&for loop

#---1---Write a Python program to check the validity of a password (input from users).

#Validation :

#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.

Password = input("Input your password")

#Do12Rs34

def Validtion(Password):

    l, u, p, d = 0, 0, 0, 0

    Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
                ,'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Characters = ['$', '#', '@']
    Numbers = "0123456789"

    if len(Password)>6 and len(Password)<16:
        for i in Password:

            # counting lowercase alphabets
            if i in alphabets:
                l += 1

            # counting uppercase alphabets
            if i in Alphabets:
                u += 1

            # counting digits
            if i in Numbers:
                d += 1

            # counting the mentioned special characters
            if i in Characters:
                p += 1

    if l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(Password):
        print("Valid Password")
    else:
        print("Invalid Password")

Validtion(Password)













