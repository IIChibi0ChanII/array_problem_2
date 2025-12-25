def maximum_profit(prices):
    if not prices and len(prices) <= 1:
        return 0
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit
    return max_profit

print(maximum_profit([6,2,20,1,8,5,9]))