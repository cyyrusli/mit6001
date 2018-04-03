import math

balance = 492
annualInterestRate = 0.15
monthlyPaymentRate = 0.05
monthlyInterestRate = annualInterestRate/12.0

def monthlyPayment(balance, PaymentRate):
    return balance * PaymentRate

def monthlyUnpaidBalance(balance, minMonthlyPayment):
    return balance - minMonthlyPayment

def updatedBalance(unpaidBalance, interestRate):
    return unpaidBalance + (interestRate * unpaidBalance)

payment = 0
# month 0
minMonthlyPayment = monthlyPayment(balance, monthlyPaymentRate)
payment += minMonthlyPayment
unpaidBalance = monthlyUnpaidBalance(balance, minMonthlyPayment)
balance = updatedBalance(unpaidBalance, monthlyInterestRate)

# month 1 - 12
for i in range(12):
    print('Month', str(i+1), 'Remaining balance: ', "%.2f" % round(balance,2))
    minMonthlyPayment = monthlyPayment(balance, monthlyPaymentRate)
    payment += minMonthlyPayment
    unpaidBalance = monthlyUnpaidBalance(balance, minMonthlyPayment)
    balance = updatedBalance(unpaidBalance, monthlyInterestRate)
