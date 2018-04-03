balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0

updatedB = balance

hi = (balance * (1 + monthlyInterestRate)**12)/12.0
lo = balance / 12

epsilon = 0.001
while(abs(updatedB - 0.0) > epsilon):
    updatedB = balance
    payment = (hi + lo) / 2.0
    for i in range(12):
        upb = updatedB - payment
        updatedB = upb + (upb * monthlyInterestRate)

    if (updatedB < 0):
        hi = payment
    elif (updatedB > 0):
        lo = payment

print('Lowest Payment:', "%.2f" % round(payment,2))