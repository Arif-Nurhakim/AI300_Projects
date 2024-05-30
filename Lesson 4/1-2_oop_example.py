# Section 1.2 Object-Oriented Programming (OOP) Example

class Stock:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def value(self):
        return self.price * self.quantity


class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, price, quantity):
        self.stocks.append(Stock(price, quantity))

    def total_value(self):
        return sum(stock.value() for stock in self.stocks)


# Data: Stock prices and quantities for each stock
stock_prices = [100, 200, 150, 300]  # Prices for each stock
stock_quantities = [10, 5, 8, 4]  # Quantities of each stock held


# Main program
portfolio = Portfolio()
for price, quantity in zip(stock_prices, stock_quantities):
    portfolio.add_stock(price, quantity)

total_value = portfolio.total_value()
print("The total portfolio value is $", total_value)
