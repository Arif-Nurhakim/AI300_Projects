# Section 1.8 Bank Account Case Study

class BankAccount:
    bank_name = "Bank of Python"   # class attribute

    def __init__(self, account_holder_name, account_number, balance):
        # instance attributes
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance


darren_account = BankAccount('Darren', 123456789, 1000)


# Bonus: Use the * asterisk to unpack lists as arguments
account_details = ['Darren', 123456789, 1000]
darren_account = BankAccount(*account_details)


# Section 1.9 Access an object's attribute
print("Account balance = $", darren_account.balance)
print("Bank =", darren_account.bank_name)


# Section 1.9 Modify an object's attribute
darren_account.balance += 2000
print("Updated account balance = $", darren_account.balance)
