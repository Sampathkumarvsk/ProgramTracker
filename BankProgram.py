class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
            print(f"Deposited {amount}. New Balance is {self.balance}")
        else:
            print("Deposit amount to be positive")


    def withdraw(self, amount):
        if amount  > self.balance:
            print("InSufficient funds")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance in {self.balance}")
        else:
            return self.balance




    def getBalance(self):
        return self.balance

account = BankAccount("johnDoe",100)
account.deposit(100)
account.withdraw(10)
print(account.getBalance())