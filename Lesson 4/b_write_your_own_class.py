# In-Class Practice: Write your own class from scratch

class CreditCard:
    def __init__(self,account_number,credit_limit):
        self.account_number = account_number
        self.credit_limit = credit_limit
        current_balance = 0
        self.current_balance = current_balance

    def get_credit_limit(self):
        return self.credit_limit

    def get_balance(self):
        return self.current_balance
    
    def set_credit_limit(self,new_limit):
        if 0 < new_limit <100000:
            self.credit_limit = new_limit
            return self.credit_limit
        else:
            print("Wrong Limit")
    
    def make_purchase(self,amount):
        if 0 < amount <= (self.credit_limit - self.current_balance):
            self.current_balance += amount
            return self.current_balance
        else:
            print("Too much spending.")
    
    def make_payment(self,amount):
        if amount > 0:
            self.current_balance -= amount
            if self.current_balance < 0:
                self.current_balance = 0
            return self.current_balance
        else:
            print("Negative payment")



# Uncomment all lines to test your class once completed

my_credit_card = CreditCard(123456789, 5000)
assert my_credit_card.account_number == 123456789
assert my_credit_card.get_balance() == 0
assert my_credit_card.get_credit_limit() == 5000

my_credit_card.set_credit_limit(1000)
my_credit_card.set_credit_limit(-1)       # print error
my_credit_card.set_credit_limit(100001)   # print error
assert my_credit_card.get_credit_limit() == 1000

my_credit_card.make_purchase(900)
my_credit_card.make_purchase(-1)          # print error
my_credit_card.make_purchase(200)         # print error
assert my_credit_card.get_balance() == 900

my_credit_card.make_payment(500)
assert my_credit_card.get_balance() == 400

my_credit_card.make_payment(5000)
assert my_credit_card.get_balance() == 0

print("All tests passed!")
