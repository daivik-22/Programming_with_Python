# Expt 3.4 – Bank Account Simulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

acc = BankAccount("Daivik", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.balance)
