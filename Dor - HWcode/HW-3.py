#---1---Create a Python script to get the largest/smallest number from a list
#---2---Create a Python script to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of strings
#---3---Create a Python script to count all the names that start with "M" from a given list

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

s=[2,5,7,3,4,6]

max = s[0]
for a in s:
    if a > max:
        max = a
print("The max number is:", max)

min = s[0]
for a in s:
    if a < min:
        min = a
print("The min number is:", min)

#---2---

words=['drd','1435','savg','11','sys','1321','10934','121']

ctr = 0
Words2=[]

for word in words:
    if len(word) > 2 and word[0] == word[-1]:
        ctr += 1
        Words2.append(word)
print(ctr)
print(Words2)

#---3---

count=0

names = ['Mor', 'Yuval', 'Many', 'Eli', 'Moshe']

for i in names:
    if i[0] == 'M':
        count += 1
print(count)


#---4---Create a Python script to calculate to price of Apple, Milk and Meat

#A

Supermerket_list={"Apple":10,"Eggs":5,"Milk":5,"Bread":3,"Meat":20}

Bill=[]

for key, value in Supermerket_list.items():
    if key == "Apple" or key =="Milk" or key =="Meat":
        Bill.append(value)
print(sum(Bill))

#B

Supermerket_list={"Apple":10,"Eggs":5,"Milk":5,"Bread":3,"Meat":20}

Bill=[]

list=["Apple","Milk","Meat"]

for key, value in Supermerket_list.items():
    if key in list :
        Bill.append(value)
print(sum(Bill))























