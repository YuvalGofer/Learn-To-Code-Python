
#Lists
list=[1,2,3,4,5]
print(list[2])
print(list[-4])
print(len(list))

#List Exercise 1.Create a Python script that Concatenate elements of a list
colors = ['red', 'green', 'orange']
len(colors)
colors.append('velvet')
print(colors[0]+ ' ' +colors[1]+ ' ' +colors[2])
#Loop is possible...


#List Exercise 2.Create a Python script that to split a given list into two parts where the length of the first part of the list is given
n_list = [1,1,2,3,4,4,5,1]
firstListLength = int(input("Enter a number"))
splitList1 = n_list[:firstListLength]
splitList2 = n_list[firstListLength:]
print(splitList1, splitList2)

#Tuple Exercise 3. Create a Python script that get the 4th element and 4th element from last of a tuple
tuplex = ("a", "v", "w", "r", "s", 7, "k", "d", 18)
print(tuplex[3], tuplex[-4])


#Tuple Exercise 4. Create a Python script that give the average value of the numbers in a given tuple of tuples
nums_1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
num1 = sum(nums_1[0]) / len(nums_1[0])
num2 = sum(nums_1[1]) / len(nums_1[1])
num3 = sum(nums_1[2]) / len(nums_1[2])
num4 = sum(nums_1[3]) / len(nums_1[3])
print(num1, num2, num3, num4)

#Dictionaries
#Exercise 1. Create a Python script  to sum all the values in a dictionary.
dict = {'Score1':12,'Score2':-4,'Score':47}
sumDict = sum(dict.values())
print(sumDict)

#Exercise 2. Create a Python script to insert two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
colorDict = {}
colorDict.update({keys[0]:values[0], keys[1]:values[1], keys[2]:values[2]})
print(colorDict)
colorDict['black']='#00001F'
print(colorDict)


#Exercise 3. Create a Python script to create a dictionary of values from a list and their power as a input number
x=[1,2,3,4,5]
n=int(input("Put a number.."))
d={x[0]:x[0]^n, x[1]:x[1]^n, x[2]:x[2]^n, x[3]:x[3]^n, x[4]:x[4]^n}
print(d)
