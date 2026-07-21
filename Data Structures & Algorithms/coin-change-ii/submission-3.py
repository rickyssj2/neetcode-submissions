from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # coins.sort() # Maybe not needed
        n = len(coins)

        # @cache
        # def dp(i, bal):
        #     if bal < 0 or i == n:
        #         return 0
        #     if bal == 0:
        #         return 1
            
        #     subcnt = 0
        #     # take the ith coin
        #     subcnt += dp(i, bal - coins[i])

        #     # skip, move to next coin
        #     subcnt += dp(i + 1, bal)

        #     return subcnt

        
        # return dp(0, amount)

        # dp[i][bal] = dp[i][bal - coins[i]] + dp[i - 1][bal]

        dp = [[0] * (amount + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(n - 1, -1, -1):
            for bal in range(1, amount + 1):
                take = dp[i][bal - coins[i]]
                skip = 0

                if bal - coins[i] < 0:
                    take = 0
                if i < n - 1:
                    skip = dp[i + 1][bal]

                dp[i][bal] = take + skip

        return dp[0][amount]

        