balance = 320000
annualInterestRate = 0.2

balance_i = balance
monthly_interest_rate = annualInterestRate / 12
monthly_payment_lower_bound = balance_i / 12
monthly_payment_upper_bound = (balance * (1+monthly_interest_rate)**12) / 12.0
e = 0.03

while abs(balance) > e:
    lowest_payment = (monthly_payment_upper_bound+monthly_payment_lower_bound)/2
    balance = balance_i
    for month in range(1, 13):
        balance = balance - lowest_payment + ((balance - lowest_payment) * monthly_interest_rate)
    if balance > e:
        monthly_payment_lower_bound = lowest_payment
    elif balance < -e:
        monthly_payment_upper_bound = lowest_payment
    else:
        break

print("Lowest Payment:", round(lowest_payment, 2))