#HW 1. create a Python script which accepts the user's first and last name and print them in reverse order with a space between them(use index())
#A
name = "Yuval Gofer"
xName = name.index(' ')
print("Hello"+ ' ' +name[xName+1:], name[:xName+0])
#B
name = "Yuval Gofer"
xName = name.split(' ')



#HW 2. create a Python script which accepts an integer (n) and computes the value of n+nn+nnn.
inputNum = int(input("Choose a number between 1-9"))
n1 = inputNum
n2 = inputNum*11
n3 = inputNum*111
print(n1 + n2 +n3 )

#HW 3. create a Python script which  get a string from a given string where all occurrences of its first char have been changed to '$',except the first char itself.
#A
userInp = input("Wrote 'Restart'")
replace = userInp.replace("r", "$", 1)
print(replace)
#B

#HW 4. create a Python script which single string from two given strings, separated by a space and swap the first two characters of each string.
#A
str1 = input("Enter first string")
str2 = input("Enter second string")
N1 = str1.replace(str1[:2], str2[:2])
N2 = str2.replace(str2[:2],str1[:2])
print(N1 + ' ' +N2)
