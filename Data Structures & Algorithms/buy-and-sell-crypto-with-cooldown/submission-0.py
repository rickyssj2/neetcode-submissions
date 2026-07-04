class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy: I am not already holding a stock and I sold more than 1 days ago
        # sell: I am holding stock and bought at least a day ago
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for hold in range(2):
                if hold: dp[i][hold] = max(prices[i] + dp[i + 2][1 - hold], dp[i + 1][hold])
                else: dp[i][hold] = max(-prices[i] + dp[i + 1][1 - hold], dp[i + 1][hold])

        # dp[i][hold] = if hold: max(prices[i] + dp[i + 2][!hold], dp[i + 1][hold])
        #               if !hold: max(-prices[i] + dp[i + 1][True], dp[i + 1][False])

        return dp[0][0]