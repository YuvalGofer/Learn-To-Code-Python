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
     print('Try agein - ')
     print('Please enter a number (print(0 to exit))')
     number = int(input("Please check the password"))

    print('You have tried', numCount, 'tries')

#Exercise 4. Create a Python script to convert a given list of lists to a dictionary with a roman letters and a name
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
def domainName(f_name, l_name, Domain):
    
    return  f_name[0:2].lower() + l_name[0:2].lower() + '@' + Domain.lower()
    
print(domainName('Yuval','Gofer', 'gmail.com'))

#Exercise 4. Create a Python script to ask if the user wants to continue to ad numbers to a list. If not, print the numbers and the sum of them

numCount = 0
numList = []
choose = input("If you like to add a number choose y..")
while choose=="y":
    nextNum = int(input('Next number:'))
    numList.append(nextNum)
    choose = input("If you like to add more number choose y..")

print('Yuor numbers are:', numList, 'The sum of your your choosen numbers are: ', sum(numList))

#Exercise 5. Create a python function to recive the Price of a lottery card the prize, the number of Balls and the number of Balls Chosen
def lottery(Price, Money, Balls_Number, Balls_Choosen):
    def Prob(Balls_Number, Balls_Choosen):
        Probs=[]
        for i in range(Balls_Number-Balls_Choosen, Balls_Number+1):
            prob = 1 / i
            Probs.append(prob)
            totalSum = 1
            for number in Probs:
                totalSum *= number
            return totalSum
    Prob=Prob(Balls_Number,Balls_Choosen)
    if Price*Prob>Money:
        return 'Take the chance'
    else:
        return 'Not worth it'
       
print(lottery(20000000,5,37,6))
 


print(lottery(2000000,5, 37,6))

#Exercise 6. Write a Python program to check the validity of a password (input from users).

#Validation :

#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.

password = input('Please enter your password.')
def passValidation(password):
  l, u, p, d = 0,0,0,0
  Alphabets = ['A', 'B', 'C','D','E','F','G','H','I','K','L','M'
             ,'N','O','P','Q','R','S','T','Y','V','W','X','Y','Z']
  alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
              ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
  Characters = ['$', '#', '@']
  Numbers = '0123456789'
  if len(password)>6 and len(password)<16:
     for i in password:
         #Counting lowercase alphabets
         if i in alphabets:
             l += 1
         #Counting uppercase alphabets
         if i in Alphabets:
             u += 1
         #Counting digits
         if i in Numbers:
             d += 1
         #Counting the mentioned special characters
         if i in Characters:
             p += 1
        
    if l >= 1 and u >= 1 and p >= 1 and d >= 1 and l+u+p+d == len(password):
      print("Valid password!")
    else:
      print("Invalid Password")

passValidation(password)
        





    multiply = lambda x, y: x*y
    print(multiply(5,6))

