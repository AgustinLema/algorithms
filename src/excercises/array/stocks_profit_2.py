from typing import List

class Solution:
    """
    I receive an array with prices for different days.
    I can only buy or sell on each day
    I can only have 1 posession, so if I have already bougth, I need to sell before buying again
    Return highest possible profit
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = None

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                if buy_price is None:
                    buy_price = prices[i]
            elif prices[i] > prices[i + 1]:
                if buy_price is not None:
                    profit += prices[i] - buy_price
                    buy_price = None
        if buy_price is not None:
            profit += prices[len(prices) - 1] - buy_price
        return profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


class Solution3:
    """
    I will always buy when the price is going to rise and sell after it stops rising,
    so I can just consider any price rise as a profit and I won't need to save buy prices
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit


class Solution4:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
