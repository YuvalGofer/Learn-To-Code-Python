#HW - Function

#HW Exe 1. Create a Python script to create and print a list where the values are square of numbers
# between 1 and n (both included)
def factore(number):
  listOfNum = []
  while (number>0):
      listOfNum.append(number**2)
      number = number-1
  return listOfNum[::-1]

print(factore(5))

#HW Exe 2. Create a Python script to find all keys in the provided dictionary that have the given value.
def keyFind(dict, val):

 keyName = []
 for key, value in dict.items():
    if value == val:
        keyName.append(key)
 return keyName

students = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
print(keyFind(students, 20))

#HW Exe 3. Create a Python script to calculate the value of the following expression by
#using lambda function.(x* 10 +( y/2 )*z)

x = 5
y = 5
z = 5
calculateNumbers = lambda x,y,z: (x*10)+(y/2)*z

print(calculateNumbers(x,y,z))

#HW Exe 4. Create a Python script to create a lambda function that multiplies argument x
#with argument y and print the result
multiplyNumbers = lambda x,y:x*y

print(multiplyNumbers(4,5))