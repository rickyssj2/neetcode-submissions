from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1, 5, 7 total = 10
        # dp[i] min number of coins needed to make total i
        # dp[i] = min(1 + dp[i - 5], 1 + dp[i - 1], 1 + dp[i - 7])
        @cache
        def dp(amount):
            if amount < 0: return float('inf')
            if amount == 0: return 0

            ans = float('inf')
            for c in coins:
                ans = min(ans, 1 + dp(amount - c))
            return ans

        ret = dp(amount)

        return ret if ret != float('inf') else -1