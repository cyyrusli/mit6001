import math

balance = 4773
annualInterestRate = 0.2

updatedBalance = balance
monthlyInterest = annualInterestRate / 12

payment = 0
increment = 10

while (updatedBalance > 0):
    updatedBalance = balance
    payment += increment
    for month in range(12):
        unpaidBalance = updatedBalance - payment
        updatedBalance = unpaidBalance + (unpaidBalance * monthlyInterest)

print ('Lowest Payment: ', payment)