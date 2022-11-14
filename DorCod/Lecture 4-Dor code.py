#Functions

factorial4 = 1
factorial7 = 1
factorial9 = 1

for i in range(1, 5):
    factorial4 *= i
for i in range(1, 8):
    factorial7 *= i
for i in range(1, 10):
    factorial9 *= i

print ('4!+7!+9!=', factorial4 + factorial7 + factorial9)

def factorial(n):

    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print ('4!+7!+9!=', factorial(4) + factorial(7) + factorial(9))

def w(x,y):

    return x*2,y*2,x**2,y**2

x=w(2,3)

print(x)

type(x)

#Palindrome

def is_palindrome_long(text):
    for i in range(1,int((len(text) / 2))+1):
        if text[i] != text[- i - 1]:
            return False
    return True


def is_palindrome_short(text):
    return text == text[::-1]

str=input(("Enter a string:"))

print(is_palindrome_long(str))
print(is_palindrome_short(str))

#Hands On

#---1---Create a Python function to check whether a number falls in a given range
#---2---Create a Python function that takes a number as a
# parameter and check the number is prime or not.
#---3---Create a Python function to reverse a string

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

def test_range(n,a,b):

    if n in range(a,b+1):
        print( n," is in the range")
    else :
        print("The number is outside the given range.")

test_range(9,1,12)

#---2---

def test_prime(n):

    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

print(test_prime(17))

#---3---

#A

def string_reverse(str1):

    rstr =str1[::-1]
    return rstr

print(string_reverse('1234abcd'))

#B

def string_reverse(str1):

    rstr = ''
    index = len(str1)
    while index > 0:
        rstr += str1[ index - 1 ]
        index = index - 1
    return rstr

print(string_reverse('1234abcd'))


#---Calculator

def calculator(x, y, op):
    if op == '+':
        return x+y
    elif op == '-':
        return x - y
    elif op == '/':
        return x/y
    elif op == '*':
        return x*y
    elif op == '**':
        return x**y
    elif op == '%':
        return x%y
    else:
        return None

print(calculator(2, 3, '**'))


def add(a, b):
    print ("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print ("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b

print ("Let's do some math with just functions!")

age = add(32, 5)
height = subtract(184, 4)
weight = multiply(40, 2)
iq = divide(180, 2)

print({"Age": age,"Height": height, "Weight": weight,"IQ": iq})

#---Functions call functions

def print_text():
    print( 'Is this the real life')
    print ('Is this the real life or it’s just fantasy')

print(print_text())

def text_2():
    print_text()
    print_text()

print(text_2())

#-----------------------------------------------

def add(a, b):
    print ("ADDING %d + %d" % (a, b))
    return a + b

print(add(2,3))

def Two_Add(a,b,c,d):

    return add(a,b),add(c,d)

print(Two_Add(2,3,3,7))

#---Default Arguments For Functions

def add(a, b=1):
    print ("ADDING",a,'+',b)
    return a + b

print(add(1, 2))

print(add(3))

print(add())

#---Function’s scope

def linear_combination(x,y):

    y = 2 * y
    return x + y

print(linear_combination(3,4))

#Hands On

#---1---Create a Python function accepts a list and determines if the elements in
# the list are integers or not
#---2---Create an inner function to calculate the addition of a

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

def print_numbers(item_list):
    for item in item_list:
        if type(item)==int:
            print(item)
        elif type(item)==list:
            print_numbers(item)
        else:
            print('No Numbers')

item_list=[5,7,'He','She',4,[1,3,4,6],4,9,'It',10]
print_numbers(item_list)

#---2---

# outer function

def outer_fun(a, b):

    square = a ** 2

# inner function
    def addition(square, b):
        return square + b

    # call inner function from outer function
    add = addition(square, b)
    # add a to the result
    return add + a

print(outer_fun(5, 8))

#Lmambda

# a simple function that returns a number multiplied by itself

def num_func (num):
    result = num ** 2
    return result

print(num_func(8))

# Same function in a lambda expression

num_lamb = lambda num: num ** 2

print(num_lamb(8))

# The basic structure of a lambda statement - lambda input: output

is_even = lambda x: x%2==0

print(is_even(98))

# lambda expression can accept multiple parameters

bigger = lambda num1, num2: num1 > num2

print(bigger(100,67))

print(bigger(100,670))

# lambda expression with if statement, for loop and while loop

#If statement

starts_with = lambda x: True if x[0]=='P' else False

print(starts_with('Python'))

print(starts_with('Java'))

#For loop

a = range(1,8)

l = lambda : [print(x) for x in a]

print(l())

#filter

nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]

total_negative_nums = list(filter(lambda n:n<0,nums))
total_positive_nums = list(filter(lambda p:p>0,nums))

print("Sum of the positive numbers: ",sum(total_negative_nums))
print("Sum of the negative numbers: ",sum(total_positive_nums))

#Hands On

#---1---Create a Python function to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number.
#---2---Create a Python function to find numbers divisible by 19 or 13 from a list of numbers using Lambda.
#---3---Create a Python function to find the elements of a given list of strings that contain specific substring using lambda.

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

n=int(input())

func_comput= lambda x: x*n

print(func_comput(2))

#---2---

nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

print("Orginal list:")
print(nums)

result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), nums))
print("\nNumbers of the above list divisible by 19 or 13:")

print(result)

#---3---

def find_substring(str1, sub_str):
    result = list(filter(lambda x: sub_str in x, str1))
    return result

colors = ["red", "black", "white", "green", "orange"]
print("Original list:")
print(colors)

sub_str = "re"

print(find_substring(colors, sub_str))

#Recursion

#Factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(4))

#fibonacci

def fibonacci_rec(n):
    if n < 2 :
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print(fibonacci_rec(13))

#---1---Create a Python function to calculate the sum of the positive
# integers of n+(n-2)+(n-4)... (until n-x =< 0).
#---2---Create a Python function to calculate the harmonic sum of n-1.

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---



def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)

print(sum_series(6))
print(sum_series(10))

#---2---

def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))


print(harmonic_sum(7))
print(harmonic_sum(1000))













