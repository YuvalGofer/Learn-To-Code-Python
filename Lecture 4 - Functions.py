#Exercise 1. Create a Python function to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_series(n):
    if n < 1:
        return 0
    else:
        # print(n)
        print(n)
        return  n + sum_series(n-2)

print(sum_series(7))
print(sum_series(8))

#Exercise 2. Create a Python function to calculate the harmonic sum of n-1.
def harminic_sum(n):
    if n <2:
        return 1
    return 1/n + harminic_sum(n-1)

print(harminic_sum(7))
print(harminic_sum(5))

#Hands on
#Exe 1. Python func to check wether a number falls in a given range
def testRange(a,b,c):
    if a in range(b,c+1):
        print(a, "Is in the range!")
    else:
        print(a, "Is not in the range")

print(testRange(8, 1, 9))

#Exe 2. Python func that takes a number as a parameter and check if prime or not
def prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
     for x in range(2, n):
        if (n % x==0):
              return False
        return True

print(prime(20))

#Exe 3. Python func to reverse a string
def testString(str):
    return str[::-1]

print(testString("Yuval"))

#Solution2 for exe 3.
def testReverseString(str):
    str2=''
    index=len(str)
    while index > 0:
        str2 += str[index-1]
        # print(str2)
        index=index-1
        # print(index)
    return  str2

print(testReverseString("Yuval"))

#Exe 4. Python func to accept a list and determine if element in the list are integers or not
def printNumberOnly(item_list):
   for item in  item_list:
       if type(item)==int:
           print(item)
       elif type(item)==list:
           printNumberOnly(item)
       else:
           print("Not a number")

item_list = [5, 7, "he", "she", 4, [1, 2, 3, 4, ], 5, "it", 10]
print(printNumberOnly(item_list))


#Exe 5. Inner func to calculate additional of :
#Outer func
def outerFunc(a, b):
    square=a ** 2

    def innerFunction(square, b):
        return square + b

    add = innerFunction(square, b)
    return  add + a

print(outerFunc(4, 6))

#Lambda example
numLambda = lambda num:num**2
print(numLambda( 2))

#Exe 6. lambda Function that take one number(argument) and multiplied unknown given number
a =range(1,5)
multipliedNumber = lambda num:[(num*x) for x in a]
print(multipliedNumber(3))
#Soloution 2 for Exe 6.
n = int(input("Enter number..."))
computeNumber = lambda x:x*n
print(computeNumber(2))

#Exe 7. lambda Function to find numbers divisible by 19 or 13 from a list
nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divideByNumber = list(filter(lambda n:n%19==0 or n%13==0, nums))
print("Numbers divisible by 19 or 13 are: ", divideByNumber)

#Exe 8. lambda Function to find element from given list of string that contain specific subsstring
def findSubString(str1, subStr):
    result = list(filter(lambda s: subStr in s, str1))
    return result

colors = ["red", "black", "white", "green", "orange"]
print("Original list: ", colors)

subStr = "bl"

print(findSubString(colors, subStr))
