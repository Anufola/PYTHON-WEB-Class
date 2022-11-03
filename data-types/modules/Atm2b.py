# solving atm app with OOP

class Atm_machine :
    def __init__(self):
        self.balance = 25000
        print("Welcome to this ATM")


    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        if amount >= 1000:
            self.balance += amount
            print("\n Amount Deposited:",amount)
        else :
            print("\nThis amount is too low for a deposit\n")

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance<=amount:
           print("\n insufficient funds")
        elif amount <= 1000:
            print("enter reasonable amount")
        else:
            print("\n withdrawal succesful")

    def checkbalance(self):
        print("\nyour current account balance is \n", self.balance)

    def transaction(self):
        print("""
        TRANSACTION 
        *********************
            Menu:
            1. Deposit
            2. Withdraw
            3. Checkbalance
            4. Exit
        *********************
        """)
        
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 :"))
            except:
                print("Error: Enter 1, 2, 3, 4\n")
                if option == 1:
                    Atm_machine.deposit()
                elif option == 2:
                    Atm_machine.withdraw()
                elif option == 3:
                    Atm_machine.checkbalance()
                elif option == 4:
                    print("Thank you for banking with us")

s = Atm_machine ()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.checkbalance()            
                 
 

        
        

