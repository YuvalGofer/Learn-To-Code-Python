#Lecture 7 - numPy
import numpy as np

#Exe 1. Create a NumPy program to create an element-wise comparison
#(greater, greater_equal, less and less_equal) of two given arrays.
x = np.array([3, 5, 7])
y = np.array([2, 5, 9])
compGre = x>=y, x<=y
print(compGre)
#Solution 2


#Exe 2. Create a NumPy program to add elements in a matrix. If an element in the matrix is 0
# ,we will not add the element below this element.
m = [[1, 1, 0, 2],
     [0, 3, 0, 3],
     [3, 0, 8, 4]]
a= np.array(m)
element_sum = 0
for p in range(len(a)):
    for q in range(len(a[p])):
        if a[p][q] == 0 and p < len(a)-1:
            a[p+1][q] = 0
            print(a)
            element_sum += a[p][q]
print(element_sum)

#Exe 3. Create a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees
# and vice versa.Values are stored into a NumPy array.
#Feahrenehit
F = np.array([0, 12, 45.21, 34, 99.91, 32])
print("Value in Feahrenehit degrees: ")
print(F)
print("Value in crntigrade: ")
print(np.array((5*(F-32))/9))
#Centigrade
C=np.array([-17.25, -11.25, 7.35, 1.87, 37.8, 0])
print("Value in centigrade: ")
print(C)
print("Value in Feahrenehit degrees: ")
print(np.array(((9*C)/5)+32))

#Pandas
#Read csv
import pandas as pd

chiptole=pd.read_excel(r"C:\Users\yuval_g\PycharmProjects\Learn-To-Code-Python\Lecture\chipotle.xlsx")
print(chiptole)
print(chiptole.head(10))
print(chiptole.tail(1))

#Exe 4. Display the ProductsName column
products = pd.read_excel(r"C:\Users\yuval_g\PycharmProjects\Learn-To-Code-Python\Lecture\Products.xlsx")
products.head()
products["ProductName"].head()

#Exe 4. Create a Python script to add 5, substras 5, divide by 10 and
#multiplay by 1.17 the unit price column
products["UnitPrice"].add(5).head()
(products["UnitPrice"] + 5).head()

products["UnitPrice"].sub(5).head()
(products["UnitPrice"]-5).head()

products["UnitPrice"].div(10).head()
(products["UnitPrice"] / 10).head()

products["UnitPrice"].mul(1.17).head()
(products["UnitPrice"]*1.17).head()

#To excel
DF1=np.random.randint(100,200,8)
DF2=np.random.randint(100,200,8)
print(DF1)
print(DF2)
type(DF1)

#Exe 1. 1.Create a Python script that take a list of positive and negative numbers and create a list of
# each type of numbers, and create a xlsx file from
themlist = [22,-5,-6,45,93,-44]
pos = []
neg = []
for i in themlist:
    if i >0:
        pos.append(i)
    else:
        neg.append(i)

print(neg, "negative")
print(pos, "positive")
df = pd.DataFrame([pos[0:len(pos)],neg[0:len(neg)]],
                  index=['pos', 'neg'],
                  columns=range(1,len(neg)+1))
df.to_excel('Positive_Negative_list.xlsx', index=False)

df2= df.T
df2.to_excel('Positive_Negative_list.xlsx', index=False)

print('End')

#Exe 2. ---
item_price=chiptole["item_price"]
item_price_discount=[]

for i in item_price:
    if i <5:
        item_price_discount.append(i)
    elif i<8:
        item_price_discount.append(i*0.9)
    else:
        item_price_discount.append(i*0.8)





