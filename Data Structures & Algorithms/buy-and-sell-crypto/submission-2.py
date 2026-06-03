class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy low, Sell high
        # [10,1,5,6,7,100]
        n, mx = len(prices), 0
        right_max = [0] * n
        # build right_max
        for i in range(n - 2, -1, -1):
            right_max[i] = max(prices[i + 1], right_max[i + 1])

        for i in range(n):
            mx = max(mx, right_max[i] - prices[i])
        return mx