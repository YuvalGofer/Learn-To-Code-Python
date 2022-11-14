#HW - List, Tuple, Dictionaries

#HW - 1
#1 . What is the fifteenth letter of the alphabet?
#2 . What is the code for the twenty-third letter of the alphabet?
#3 .  What is the fourth letter of the code for the eighth letter of the alphabet?
Alphabet = [
        ["A", "Alfa"],
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
        ["Z", "Zulu"]
    ]
print(Alphabet[14])
print(Alphabet[22][1])
print(Alphabet[7][1][3])

#HW - 4. Create a Python script that to Convert a given tuple of positive integers into an integer
nums=(1,2,3)
combine = nums[0]*100+nums[1]*10+nums[2]
print(combine)

#HW - 5. Create a Python script that change the first elemant in a tuple
x = ("apple", "banana", "cherry")
switch = list(x)
switch[0] = 'kiwi'
x = tuple(switch)
print(x)

#HW - 6. Create a Python script that combine values in python list of dictionaries.
results ={}
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}]
item1 = {item_list[0]['item']: item_list[0]['amount']}
item2 = {item_list[1]['item']: item_list[1]['amount']}
results.update(item1)
results.update(item2)
print(results)

