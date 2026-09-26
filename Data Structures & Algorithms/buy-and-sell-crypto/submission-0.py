class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        before = []
        profit = []
        for i in range(len(prices)):
            if i + 1 == len(prices):
                break
            for j in range(i + 1, len(prices)):
                dif = prices[j] - prices[i]
                profit.append(dif)
            maxp = max(profit)
            before.append(maxp)
        if not before:
            return 0
        net_profit = max(before)
        if net_profit > 0:
            return net_profit
        else:
            return 0
