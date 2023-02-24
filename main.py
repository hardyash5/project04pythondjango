amount = 1000
portfolio = 0
money_end = amount
investment = []
transaction_cost = 0.0075

def buy(quantity, price):
    global portfolio, money_end
    allocated_money = quantity*price
    money_end = money_end - allocated_money - transaction_cost*allocated_money
    portfolio += quantity

    if investment ==[]:
        investment.append(allocated_money)
    else:
        investment.append(allocated_money)
        investment[-1] += investment[-2]

def sell(quantity, price):
    global portfolio, money_end
    allocated_money = quantity*price
    money_end = money_end + allocated_money - transaction_cost * allocated_money
    portfolio -= quantity
    investment.append(-allocated_money)
    investment[-1] += investment[-2]