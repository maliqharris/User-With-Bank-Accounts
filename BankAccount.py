class BankAccount:
    
    def __init__(self, int_rate, balance): 
       self.int_rate = int_rate
       self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print("Interest Rate:",self.int_rate)
        print("Balance:",self.balance)
    def yield_interest(self):
        self.balance = self.balance - (self.balance * self.int_rate)
        return self
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        print(self.account.balance)


User1 = User("Maliq", "coolguy@gmail.com")
User1.make_deposit(20)
User1.display_user_balance()

# Account1 = BankAccount(.05, 100)
# Account2 = BankAccount(.07, 5)
# # Account1.deposit(10).deposit(10).deposit(10).withdraw(10).display_account_info()
# Account2.deposit(100).deposit(100).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()
