account = {"balance":2500}

def deposit(acc, amt):
    if amt >= 1000:
        acc["balance"] += amt
        print("n", amt, "successfully deposited to your account deposited to your account\n")
    else:
        print("\nThis amount is too low for a deposit\n")

def withdraw(acc, amt):
    if amt >= 1000 and amt < acc["balance"]:
        acc["balance"] -= amt
        print("\n", amt, "succesfully withdrawn from your account\n")
    elif amt < 1000:
        print("\nThis amount is too low for withdrawa\n")
    elif amt > acc["balance"]:
        print("\ninsufficient balanve!\n")

def check_balance(acc):
    print("\nYou have" "acc"["balance"], "left in your account\n")