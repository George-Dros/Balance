balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0

for month in range(12):
    balance = balance - (balance * monthlyPaymentRate) + (
            (balance - (balance * monthlyPaymentRate)) * (annualInterestRate / 12))

final_balance = balance.__round__(2)
print("Remaining balance:", final_balance)


