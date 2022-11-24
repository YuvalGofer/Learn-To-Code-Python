#Exercise 1. Create a Python function to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_series(n):
    if n < 1:
        return 0
    else:
        return n + sum_series(n-2)

print(sum_series(6))
print(sum_series(8))

#Exercise 2. Create a Python function to calculate the harmonic sum of n-1.
def harminic_sum(n):
    if n <2:
        return 1
    return 1/n + harminic_sum(n-1)

print(harminic_sum(7))
print(harminic_sum(5))


