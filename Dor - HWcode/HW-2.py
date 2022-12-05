#Home work

#---list---

#---1---What is the fifteenth letter of the alphabet?
#---2---What is the code for the twenty-third letter of the alphabet?
#---3---What is the fourth letter of the code for the eighth letter of the alphabet?

Alphabet = [["A", "Alfa"],
          ["B", "Bravo"],
          ["C", "Charlie"],
          ["D", "Delta"],
          ["E", "Echo"],
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
          ["Q", "Quebec"],
          ["R", "Romeo"],
          ["S", "Sierra"],
          ["T", "Tango"],
          ["U", "Uniform"],
          ["V", "Victor"],
          ["W", "Whiskey"],
          ["X", "X-ray"],
          ["Y", "Yankee"],
          ["Z", "Zulu"]]

# 1. - 15th letter is: ["O", "Oscar"]

print(Alphabet[14][0])

# 2. - 23rd letter is: ["W", Whiskey]

print(Alphabet[22][1])

# 3. - 8th letter is: ["H", "Hotel"]

print(Alphabet[7][1][3])

#Tuples

#---4---Create a Python script that Convert a given tuple of positive integers into an integer

#A

nums = (1, 2, 3)

combine = nums[0] * 100+nums[1] * 10 + nums[2]

print(combine)

#B

nums =(1,2,3)

a=nums[0]

a=a.__str__()

b=nums[1]

b=b.__str__()

c=nums[2]

c=c.__str__()

print(int(a+b+c))

#---5---Create a Python script that change the first elemant in a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[0] = "kiwi"
x = tuple(y)

print(x)

#---6---Create a Python script that combine values in python list of dictionaries

#Dictionaries

#A

item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}]

result={}

item_1={item_list[0]['item']: item_list[0]['amount']}
item_2={item_list[1]['item']: item_list[1]['amount']}

result.update(item_1)
result.update(item_2)

print(result)

#B

item_list = [{'item' : 'item1', 'amount' : 400}, {'item' : 'item2', 'amount' : 300}]

new_item_dict = {}

first_item = list(item_list[0].values())
second_item = list(item_list[1].values())

new_item_dict.update({first_item[0]: first_item[1]})
new_item_dict.update({second_item[0]: second_item[1]})

print(new_item_dict)