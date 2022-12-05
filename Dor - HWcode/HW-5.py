#---1---Create a Python function get 1 argument a returns
# 3 results(number+1' number*3 and (number*3)**number
#---2---Create a Python function get amount of loan,rate, a 2 durations,
#and if the gap between the monthly payments is less than 200 and the
# gap between the total returns are more than 1000, the first loan in better

#-----------------------------------#
# Solutions
#-----------------------------------#

#---1---

def get_a_lot(x):
    y0 = x + 1
    y1 = x * 3
    y2 = y1 ** x
    return (y0, y1, y2)

print(get_a_lot(2))

#---2---

def loan_emi(amount, duration_1,duration_2, rate):

    Monthly_payment_1=round((amount*(1+rate)**duration_1)/(duration_1*12))
    Monthly_payment_2=round((amount * (1 + rate) ** duration_2) / (duration_2 * 12))
    Total_return_1=round((amount*(1+rate)**duration_1))
    Total_return_2=round((amount * (1 + rate) ** duration_2))
    if Monthly_payment_1-Monthly_payment_2<200 and Total_return_1-Total_return_2>1000:
        return "Loan 1 is better"
    else:
        return "Loan 2 is better"

print(loan_emi(10000, 2,5, 0.02))