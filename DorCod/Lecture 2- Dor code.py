#Lists

list = [9,8,6,1,5]

print(list)

print(list[::-1])

print(list[0])

print(list[4])

print(list[-3])

print(list[::2])

print(list[5])

#Reverse

print(list[::-1])

Days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

print(Days)

print(Days[5])

#Dynamic lists

students = ['Sharon',9654520, 'Liat',837561405 ,'Yaniv',968554353]

print(students[2])

#Append

students.append('Roze')

print(students)

#Remove

students.remove('Yaniv')

print(students)

#Assigments

list_1= [1,2,3]
list_2= list_1
list_1 = [6,7,8,9]

print(list_2)

print(list_1)

#---------------------------------

list_2= list_1
list_1[0] = 1000

print(list_1)

print(list_2)

#Nested lists

NL=[[3, 7, 2],[6, 0, 1]]

print(NL[1])

print(NL[1][0],NL[0][2])

len(NL)

#Hands On

#---1---Create a Python script that Concatenate elements of a list
#---2---Create a Python script that to split a given list into two parts
# where the length of the first part of the list is given

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

colors = ['red', 'green', 'orange']

print(colors[0]+colors[1]+colors[2])

print(colors[0]+' '+colors[1]+' '+colors[2])

#---2---

n_list = [1,1,2,3,4,4,5,1]

first_list_length = int(input("Enter a number:"))

Split_1=n_list[:first_list_length]
Split_2=n_list[first_list_length:]

print(Split_1,Split_2)

#Tuples

#Lists are mutable

my_list = [1,2,3]

print(my_list)

my_list[1]=10

print(my_list)

my_tuple = (1,2,3)

print(my_tuple)

my_tuple[1]=10

#Tuples are immutable lists

B = ("Let",'It','be') # definition

print(B[0])  	# indexing

print(B[-1])	# backwords indexing

print(B[1:2]) 	# slicing

my_tuple = (1,2,3)

print(sum(my_tuple))#Sum

#Hands On

#---1---Create a Python script that get the 4th element and 4th element from last of a tuple
#---2---Create a Python script that give the average value of the numbers in a given tuple of tuples

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

tuplex = ("a", "v", "w", "r", "s", 7, "k", "d", 18)

print(tuplex)

item = tuplex[3]
item1 = tuplex[-4]

print(item,item1)

#---2---

nums_1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

Avg_1=sum(nums_1[0]) / len(nums_1[0])
Avg_2=sum(nums_1[1]) / len(nums_1[1])
Avg_3=sum(nums_1[2]) / len(nums_1[2])
Avg_4=sum(nums_1[3]) / len(nums_1[3])

print(Avg_1,Avg_2,Avg_3,Avg_4)

#Dictionaries

ID_list = {'Eric': '30145', 'Shlomi': '38171', 'Kobi': '85736'}

print(ID_list)

print(ID_list['Eric'])

ID_list['David'] = '84759'

print(ID_list)

ID_list ['David']= '75647'

print(ID_list)

print(ID_list['Eric'])
print(ID_list.get('Eric'))

ID_list['Amir'] = '23894'

print(ID_list)

ID_list.update({"Amir": "23894","Yoni":"92840"})

print(ID_list)

ID_list.items()
ID_list.keys()
ID_list.values()
ID_list.pop('David')

print(ID_list)

#Hands On

#---1---Create a Python script  to sum all the values in a dictionary.
#---2---Create a Python script to insert two lists into a dictionary.
#---3---Create a Python script to create a dictionary of values from a list and their power as a input number

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

dict = {'Score1':12,'Score2':-4,'Score':47}

print(sum(dict.values()))

#---2---

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

color_dictionary={}

color_dictionary[keys[0]]=values[0]
color_dictionary[keys[1]]=values[1]
color_dictionary[keys[2]]=values[2]

color_dictionary.update({keys[0]: values[0]})
color_dictionary.update({keys[1]: values[1]})
color_dictionary.update({keys[2]: values[2]})

color_dictionary.update({keys[0]: values[0],
                        keys[1]: values[1],
                        keys[2]: values[2]})

print(color_dictionary)

#---3---

x=[1,2,3,4,5]

n=int(input())

d={x[0]:x[0]**n,x[1]:x[1]**n,x[2]:x[2]**n,
   x[3]:x[3]**n,x[4]:x[4]**n}

print(d)


















