import person as p

print(p.person["name"])
print(p.person["concubines"])

# dir
y = dir(p)
print(y)

# Assignment 3:
# Using modules, simulate an ATM machine that can deposit money, withdraw and check balance
#it should be menu driven
# e.g
# 1. Deposit
# 2. Withdrawal
# 3. Check Balance
# Starting balance in the account should be 25000
# Note: You cannot withdraw or deposit money lesss than 1000 and 
# you cannot withdraw more than what you have in your account