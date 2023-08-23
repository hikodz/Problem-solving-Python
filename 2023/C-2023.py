def tax_collector():
    days = int(input('|=> '))
    prices = []
    for _ in range(days):
        price = int(input('|> '))
        prices.append(price)
    position_min = prices.index(min(prices))
    del prices[:position_min]
    prices.sort()
    return prices[-1] - prices[0]
print(tax_collector())
