

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):

        if self.balance > amount:
            self.balance -= amount
        else:
            print("insufficient balance")

    def display_balance(self):
        print("account holder: ",self.name)
        print("balance: ",self.balance)

account1 = BankAccount("Mukesh",100000000000)

account1.display_balance()
account1.deposit(300000000000)
account1.withdraw(21000000)
account1.display_balance()