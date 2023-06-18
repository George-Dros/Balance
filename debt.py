balance = 3926
annualInterestRate = 0.2

monthly_interest_rate = annualInterestRate / 12.0
balance_i = balance
lowest_payment = 10

while balance > 0:
    for month in range(1,13):
        balance -= lowest_payment
        balance = balance*(1 + monthly_interest_rate)
    if balance > 0:
        balance = balance_i
        lowest_payment += 10

print("Lowest Payment:", lowest_payment)