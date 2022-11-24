#Lecture 5 - Review

#Exercise 3. Create a script will get numbers from user until users enters 0. Program will print how many tried the user made
numCount = 0
passInput = int(input("Please choose a password - 4 digit please "))
print('Please enter a number to check password (print(0 to exit))')
number = int(input("Your number here..."))
while number != 0:
    if number == passInput:
        print('You are right!')
        break
    else:
     numCount +=1
     print('Please enter a number (print(0 to exit))')
     number = int(input("Please check the password"))

    print('You have tried', numCount, 'tries')

#Exercise 2. Create a Python script to convert a given list of lists to a dictionary with a roman letters and a name
def test(lst):
    Dict_list = {}
    for x,y,z in lst:
        Dict_list[x]=z
        return Dict_list
students = [['Jean Castro',1, 'V'], ['Lula Powell',2,  'V'],
            ['Brian Howell',3,  'VI'], ['Lynne Foster',4,  'VI'],
            ['Zachary Simon',5,  'VII']]
print(test(students))

#Exercise 3.Create a Python function to recive a first name, last name and an email domain(
#gmail.com, hitmail.com etc. and create a maul accounts from the 3 first letters form the
#first name(lower case), 3 first letters form the last name(lower case) and from the email domain
def domainName(fName, lName, Domain):

#Exercise 4. Create a Python script to ask if the user wants to continue to ad numbers to a list. If not, print the numbers and the sum of them
numCount = 0
numList = []
choose = input("If you like to add a number choose y...")
while choose=="y":
    num = int(input('Next number...'))
    numList.append(num)
    choose = input("If you like to add a number choose Y...")
    print('Yuor numbers are:', )


#Exercise 5. Create a python function to recive the Price of a lottery card the prize, the number of Balls and the number of Balls Chosen


Probs = []
for i in range(31, 38):
    prob = 1 / i
    Probs.append(prob)
    totalSum = 1
    for number in Probs:
        totalSum *= number
print(totalSum)

#Exercise 6. Write a Python program to check the validity of a password (input from users).

#Validation :

#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.
password = input('Please enter your password.')
def passValidation(password):

    multiply = lambda x, y: x*y
    print(multiply(5,6))

