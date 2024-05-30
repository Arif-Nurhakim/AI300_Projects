# Section 1.1 Procedure to calculate total portfolio value

def calculate_portfolio_value(prices, quantities):
    total_value = 0
    for price, quantity in zip(prices, quantities):
        total_value += price * quantity
    return total_value


# Data: Stock prices and quantities for each stock
stock_prices = [100, 200, 150, 300]  # Prices for each stock
stock_quantities = [10, 5, 8, 4]  # Quantities of each stock held


# Main program
total_value = calculate_portfolio_value(stock_prices, stock_quantities)
print("The total portfolio value is $", total_value)
