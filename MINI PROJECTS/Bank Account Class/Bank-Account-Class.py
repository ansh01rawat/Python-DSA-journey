class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount > 0
        self.balance += amount

    def withdraw(self,amount):

        if self.balance > amount:
            self.balance -= amount
        elif amount <= 0:
            print("invalid amount")
        else:
            print("insufficient balance")

    def display_balance(self):
        print("account holder: ",self.name)
        print("balance: ",self.balance)

account1 = BankAccount("Mukesh",100000000000)
account2 = BankAccount("Tata",1000000000)

account1.display_balance()
account1.deposit(300000000000)
account1.withdraw(21000000)
account1.display_balance()

account2.display_balance()
account2.deposit(300000000000)
account2.withdraw(21000000)
account2.display_balance()
