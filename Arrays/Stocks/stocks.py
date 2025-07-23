def maxProfit(prices):
    mini=prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        mini = min(mini, prices[i])
        max_profit = max(max_profit, prices[i] - mini)
    return max_profit

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(maxProfit(prices))