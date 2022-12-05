#Matplotlib & TKint
import numpy as np
import  matplotlib.pyplot as plt
import random as rd
import pandas as pd

#Exe 1. Create a Python script that Read the Total profit of all months and show it using a line plot
sales = pd.read_excel(r"C:\Users\yuval_g\PycharmProjects\Learn-To-Code-Python\Lecture\sales_data.xlsx")
sales.head()
print(sales)
totalPro = sales["total_profit"].tolist()
monthNum = sales["month_number"].tolist()
print(totalPro, monthNum)
plt.plot(monthNum,totalPro)
plt.xlabel('Month')
plt.ylabel('Total profit')
plt.title('Month & Profit')
plt.show()

#Exe 2.Create a Python script that Read toothpaste sales data of each month and show it using a scatter plot
monthNum = sales["month_number"].tolist()
toothPasteSalesData=sales["toothpaste"].tolist()
plt.scatter(monthNum,toothPasteSalesData, label='Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units sold')
plt.legend(loc='upper left')
plt.xticks(monthNum)
plt.show()

#Exe 3.Create a Python script that Calculate total sale data for last year for each product and show it using
# a Pie chart
#--plt.pie(salesData, labels=labels, autopct='%1.1f%%')
monthNum = sales["month_number"].tolist()
labels = ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
salesData = [sales['facecream'].sum(),sales['facewash'].sum(),sales['toothpaste'].sum(),sales['bathingsoap'].sum(),
            sales['moisturizer'].sum(),sales['shampoo'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='center left')
plt.title('Sales data')
plt.show()

#tkinter
import tkinter as tk
#Exe 1. create a window and set its title.

from tkinter import *
window = Tk()
window.title("Hi there")
window.minsize(400,400)
window.mainloop()
#Exe 2. create a window. Set its title and add a label to the window.
from tkinter import *
window = Tk()
window.title("Hi there")
window.minsize(400,400)
my_label=Label(text="Hi there")
my_label.pack()
window.mainloop()
#Exe 3. create a label and change the label font style (font name, bold, size)
#sing tkinter module.
from tkinter import *
window = Tk()
window.title("Font change")
window.minsize(400,400)
my_label=Label(text="How is't now?", font=('Arial', 35, "bold"))
my_label.pack()
window.mainloop()

#Exe 4. create a window and set the default window size using tkinter module.
from tkinter import *
window = Tk()
window.title("Default size")
window.minsize()
window.mainloop()

#Exe 5. create a window and disable to resize the window using tkinter module.


window = Tk()
window.title("Disable resize")
window.resizable(0,0)
window.mainloop()
#Exe 6. create a Text widget using tkinter module.Insert a string at the beginning then insert a string into the current text.
window =Tk()
