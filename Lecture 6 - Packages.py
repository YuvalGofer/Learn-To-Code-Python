#randome
import random as rd

print(rd.randrange(100))
print(rd.randrange(10,100))
print(rd.randrange(10,100,3))

print(rd.choice(["apple", "banana", "cherry"]))
print(rd.choice('Pink Floyd'))
Choices_list=rd.choices([97,34,44] ,weights = [5, 2, 1], k = 140)

print(Choices_list)

print(Choices_list.count(97))
print(Choices_list.count(34))
print(Choices_list.count(44))

Choices_list_2=rd.choices(["M","F"] ,weights = [2,3], k = 20)
print(Choices_list_2)

print(Choices_list_2.count("M"))
print(Choices_list_2.count("F"))


lst = ["apple", "banana", "cherry"]

print(lst)

str='ace two three four'
deck = str.split()
rd.shuffle(deck)
print(deck)


Students = ["Yeal","Libi","David","Daniel","Valary","Noam",
            "Yuval","Liat","Alaa","Avi","Itay","Tal"]

print(rd.sample(Students, 2))

import matplotlib.pyplot as plt

# store the random numbers in a list

nums = []
mu = 120
sigma = 45

for i in range(100):
    temp = rd.gauss(mu, sigma)
    nums.append(temp)

# plotting a graph

plt.plot(nums)
plt.show()

#Hands on

#---1---Create a Python script to generate a random integer between 0 and 6 -
# excluding 6, random integer between 5 and 10 excluding 10, random integer between 0 and 10, with a step of 3
#---2---Create a Python script to Choose random name form a list
#---3---Create a Python script to generate a guessing number game, allowing the user a
# limited of 7 guesses, using input from user and randint function

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

print(rd.randrange(6))

print(rd.randrange(5,10))

print(rd.randrange(0, stop=10, step=3))

#---2---

Choose_Name = ["James","John","Mark","Rick"]

print(rd.choice(Choose_Name))

Choose_Name = ["James","John","Mark","Rick"]
# print("Original list: ", Choose_Name)
for i in range(1,5):
    chosen = rd.choice(Choose_Name)
    print(chosen)
    Choose_Name.remove(chosen)
    break

print(Choose_Name)

#---3---

def Guesses(GUESSESALLOWED) :

    n = rd.randint (1,10)
    guesses = 0
    while guesses < GUESSESALLOWED :
        guess = int( input (" Enter an integer 1 to 10: " ))
        if guess < 1 or guess > 11:
            print ( " That ’s an illegal guess . Try again !" )
        elif guess == n:
            print ( " Congratulations ! You took " , \
                        guesses + 1, " guesses ! " )
            return
        elif guess < n:
            print ( " Guess is too low . Try again !" )
        else :
            print ( " Guess is too high . Try again !" )

        guesses += 1

    print ( " Whoops ! You took too many guesses ." , \
            " The answer was " , n )

Guesses(7)

#Datetime

import datetime

Day=rd.randrange(1,29)
Month=rd.randrange(1,13)
Year=rd.randrange(1990,2022)

Date=datetime.date(Year,Month,Day)

print(Date)

type(Date)

#Replace day, month and year

New_Date=Date.replace(day=7)

print(New_Date)

New_Date=New_Date.replace(month=10)

print(New_Date)

New_Date=New_Date.replace(year=1992)

print(New_Date)
print(Date)

#strftime

#Day in short format
Date.strftime("%a")

#Day in long format
Date.strftime("%A")

#Day in number
Date.strftime("%d")

#Day in date format
Date.strftime("%D")

#The number of the day in a year
Date.strftime("%j")

#The number of the week in a momth(index)
Date.strftime("%w")

#The number of the week  in a year
Date.strftime("%W")

#Month in short format
Date.strftime("%b")

#Month in lomg format
Date.strftime("%B")

#Year in short format
Date.strftime("%y")

#Year in long format
Date.strftime("%Y")

#Today

Today=datetime.date.today()

print(Today)

type(Today)

#Timedelta

Date=Today-datetime.timedelta(weeks=5)
print(Date)
Date=Today-datetime.timedelta(days=8)
print(Date)
Date=Today-datetime.timedelta(hours=24)
print(Date)
Date=Today-datetime.timedelta(minutes=3000)
print(Date)

#Date formats

str_date =Date.strftime('%d/%m/%y')

print(str_date)

type(str_date)

str_date = Date.strftime("%Y%m%d")

print(str_date)

str_date = Date.strftime("%y%m%d")

print(str_date)

str_date = Date.strftime("%y.%m.%d")

print(str_date)

str_date = Date.strftime("%y-%m-%d")

print(str_date)

str_date = Date.strftime("%Y/%m/%d")

print(str_date)

str_date = Date.strftime("%d%m%Y")

print(str_date)

str_date = Date.strftime("%m.%d.%Y")

print(str_date)

#Sleep

import time

for x in range(5):
   time.sleep(3)
   print("Sorry, Slept for 3 seconds...")
print("End")


for x in range(3):
   time.sleep(2)
   Students = ["Yeal","Libi","David","Daniel",
            "Valary","Noam","Yuval","Liat",
            "Alaa","Avi","Itay","Tal",
            "Michel","Alon","Elad","Bar",
            "Sharon", "Noa", "Maia", "Tomer"]

   def Rooms(list):

        Room_1 = rd.sample(list, 4)
        for i in Room_1:
            if i in list:
                list.remove(i)

        Room_2 = rd.sample(list, 4)
        for i in Room_2:
            if i in list:
                list.remove(i)

        Room_3 = rd.sample(list, 4)
        for i in Room_3:
            if i in list:
                list.remove(i)

        Room_4 = rd.sample(list, 4)
        for i in Room_4:
            if i in list:
                list.remove(i)

        Room_5 = list


        return Room_1,Room_2,Room_3,Room_4,Room_5

   print(Rooms(Students))

#---Write a Python program to print a string five times, delay three seconds.

x=0

print("This will print five  times, delay for three seconds.")

while x<4:
    print("My precious")
    time.sleep(2)
    x=x+1

print("End")

x=0

print("This will print five  times, delay for three seconds.")
while x<3:
    n = rd.randint(2, 5)
    print("My precious")
    time.sleep(n)
    x=x+1

print("End")

#Time zone

import pytz

unaware = datetime.datetime.now()
print(unaware)
print('Timezone naive:', unaware)

# Convert unaware Datetime to UTC timezone aware Datetime

aware = unaware.replace(tzinfo=pytz.UTC)
print(aware)

dt_us_pacific = datetime.datetime.now(pytz.timezone('America/Tijuana'))
print("US Pacific timezone DateTime:", dt_us_pacific.strftime("%Y:%m:%d %H:%M:%S"))

dt_us_eastern = datetime.datetime.now(pytz.timezone('America/New_York'))
print("US Eastern timezone DateTime:", dt_us_eastern.strftime("%Y:%m:%d %H:%M:%S"))

#Hands on

#---1---Create a Python script to print yesterday, today, tomorrow dates.
#---2---Create a Python script to get days between two dates.
#---3---Create a Python script to check how many days are in the month of today date

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

Today=datetime.date.today()
yesterday = Today - datetime.timedelta(days = 1)
tomorrow = Today + datetime.timedelta(days = 1)

print('Yesterday : ',yesterday)
print('Today : ',Today)
print('Tomorrow : ',tomorrow)

#---2---

a = datetime.date(2000,2,28)
b = datetime.date(2001,1,4)

print(b-a)

#---3--

Mon_31=['Jan','Mar','May','Jul','Aug','Oct','Dec']
Mon_30=['Apr','Jun','Sep','Nov']

Today=datetime.date.today()

Today.strftime("%b")

if Today.strftime("%b") in Mon_31:
    print("It's a 31 days month")
elif Today.strftime("%b") in Mon_30:
    print("It's a 30 days month")
else:
    print("It's February :(")

#OS

import os

#Walk

path = 'C:\\Users\\USER\Desktop\Dor\מסמכים\עצמאי\האקריו\הרצאות\PDF luctures'

for root, dirs, files in os.walk(path):
    print(root,"is root")
    for _dir in dirs:
        print(_dir,"is dir")
    for _file in files:
        print(_file,"is file")

#splite&join

path = r'C:\\Users\\USER\Desktop\Dor\מסמכים\\האקריו\\הרצאות\Dimoand.xlsx'
print("Original path:")
print(path)
print("\nDir and file name of the said path:")
print(os.path.split(path))
print("\nJoin one or more path components together:")
print(os.path.join(r'C:\\Users\\USER\Desktop\Dor\מסמכים\\האקריו\\הרצאות','Dimoand.xlsx'))

#listdir

path = 'C:\\Users\\USER\Desktop\Dor\מסמכים\עצמאי\האקריו\הרצאות'
print(os.listdir(path))
print(os.path.isdir(path))
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])

path = 'C:\\Users\\USER\Desktop\Dor\מסמכים\עצמאי\האקריו\הרצאות'

print(os.scandir(path))

for entry in os.scandir(path):

   if entry.is_dir():
       typ = 'dir'
   elif entry.is_file():
       typ = 'file'
   elif entry.is_symlink():
       typ = 'link'
   else:
       typ = 'unknown'
   print('{name} {typ}'.format(
       name=entry.name,
       typ=typ,
   ))

os.rename(r"C:\Users\USER\PycharmProjects\Lectures\Dimoand.csv"
        ,"C:\\Users\\USER\Desktop\Dor\מסמכים\עצמאי\האקריו\הרצאות\Dimoand.csv")

print("End")

#Shutil

import shutil

#Copyfile

shutil.copyfile(r"C:\Users\USER\PycharmProjects\Lectures\posneg.xlsx"
                ,r"C:\Users\USER\PycharmProjects\Lectures\Positive_Negative_list.xlsx")
print("End")

#copy

shutil.copy("C:\\Users\\USER\PycharmProjects\Lectures\posneg.xlsx"
            ,"C:\\Users\\USER\Desktop\Dor\מסמכים\עצמאי\האקריו\הרצאות\posneg.xlsx")

print("End")

#move

shutil.move("C:\\Users\\USER\PycharmProjects\Lectures\posneg.xlsx"
            ,"C:\\Users\\USER\Desktop\Dor\מסמכים\עצמאי\האקריו\הרצאות\posneg.xlsx")

print("End")

#copytree

shutil.copytree("C:\\Users\\USER\Desktop\Dor\מסמכים\עצמאי\האקריו\\src",
                "C:\\Users\\USER\Desktop\Dor\מסמכים\עצמאי\האקריו\\dest")

print("End")

#---Hans on

#---1---Create a Python script to take a directory form of the first day of the month
# and create a directories of all the days in the month

shutil.copytree(r"C:\Users\USER\Desktop\Dor\מסמכים\האקריו\11\011122",
                r"C:\Users\USER\Desktop\Dor\מסמכים\האקריו\\dest")


def dir_creator(path,month):

    i=2
    while i<=31:
        if i<10:
            src=path+'\\'+str(month)+'\\'+'0'+str(i-1)+str(month)+'22'
            dest=path+'\\'+str(month)+'\\'+'0'+str(i)+str(month)+'22'
            shutil.copytree(src,dest)
        elif i==10:
            src = path+'\\'+str(month) + '\\' +'0'+ str(i - 1)+str(month)+'22'
            dest = path+'\\'+str(month) + '\\'+ str(i)+str(month)+'22'
            shutil.copytree(src, dest)
        else:
            src = path+'\\'+str(month)+ '\\'+ str(i - 1)+str(month)+'22'
            dest =path+'\\'+str(month) + '\\' + str(i) +str(month)+'22'
            shutil.copytree(src, dest)
        i+=1
    print("End")

dir_creator('C:\\Users\\USER\Desktop\Dor\מסמכים\עצמאי\האקריו',11)




def copyDir(path,month):

    x=0
    if (month in ['1', '3', '5', '7', '8', '10', '12']):
        amount=31;
        for i in range(1,amount+1):
            shutil.copytree(path + '\\' +str(month)+ '\\' + str((0))+ str((i)) + str(month) + '22',
                            path + '\\' +str(month)+ '\\' + str((0))+str((i + 1)) + str(month) + '22')
    elif(month in ['4','6','9','11']):
        amount=30
        for i in range(1,amount+1):
            shutil.copytree(path + '\\' +str(month)+ '\\' + str((0))+ str((i)) + str(month) + '22',
                            path + '\\' +str(month)+ '\\' + str((0))+str((i + 1)) + str(month) + '22')
    else:
        amount = 28
        for i in range(1,amount+1):
            shutil.copytree(path + '\\' +str(month)+ '\\' + str((0))+ str((i)) + str(month) + '22',
                            path + '\\' +str(month)+ '\\' + str((0))+str((i + 1)) + str(month) + '22')
    x+=1
copyDir('C:\\Users\\USER\Desktop\Dor\מסמכים\האקריו',11);
