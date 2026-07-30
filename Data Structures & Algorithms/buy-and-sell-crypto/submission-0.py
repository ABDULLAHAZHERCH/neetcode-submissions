class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        buy = prices[0]
        for sell in prices:
            p = max(p,sell-buy)
            buy = min(buy,sell)
        return p