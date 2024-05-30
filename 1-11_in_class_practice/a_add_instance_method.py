# In-Class Practice: Add an instance method

class BankAccount:
    bank_name = "Bank of Python"   # class attribute

    def __init__(self, account_holder_name, account_number, balance):
        # instance attributes
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient Funds")
        pass


# Uncomment to test your class once completed

my_account = BankAccount('Darren', 123456789, 1000)
my_account.withdraw(100)
print(my_account.balance)  # should print 900

my_account = BankAccount('Darren', 123456789, 10)
my_account.withdraw(100)   # should print error message
print(my_account.balance)  # should print 10
