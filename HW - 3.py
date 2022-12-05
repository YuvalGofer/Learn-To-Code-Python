#HW - 3
#HW - 1. Create a Python program to get the largest/smallest number from a list
s=[9,5,7,3,4,6]
max = s[0]
# print(max)
for a in s:
    if a > max:
        max = a
        print("The max number is:", max)

min = s[0]
for a in s:
    if a <min:
        min = a
        # print(min)
        print("The min number is:", min)

print(max, min)
#HW 2. Create a Python program to count the number of strings where the string length is 2 or
#more and the first and last character are same from a given list of strings

words=['drd','1435','savg','11','sys','1321','10934','121']

count = 0
newWord = []
for word in words:
 if len(word)>2 and word[0] == word[-1]:
     count +=1
     newWord.append(word)
print(count)
print(newWord)

#HW 3. Create a Python program to count all the names that start with "M" from a given list
names = ['Mor','Yuval', 'Many','Eli','Moshe']
nameM = []
count2 = 0
for letter in names:
 if letter[0]=='M':
     count2+=1
     nameM.append(letter)

print(count2)
print(nameM)

#HW 4. Create a Python script to calculate to price of Apple, Milk and Meat

Supermerket_list ={"Apple": 10 ,"Egg": 5 ,"Milk": 5 ,"Meat": 3 ,"Bread": 20}
Bill=[]
list=["Apple", "Egg","Bread"]
for key, value in Supermerket_list.items():
    if key in list:
        Bill.append(value)

print(sum(Bill))
