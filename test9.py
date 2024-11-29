def max_stocks(stocks, max_limit):
    dp = [0] * (max_limit + 1)

    for stock in stocks:
        for i in range(max_limit, stock - 1, -1):
            dp[i] = max(dp[i], dp[i - stock] + stock)

    return dp[max_limit]


stocks = [30, 30, 40]
max_limit = 65

print(max_stocks(stocks, max_limit))
