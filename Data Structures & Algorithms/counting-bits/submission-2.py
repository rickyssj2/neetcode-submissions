class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        dp = [0] * (n + 1) # dp[i] is the number of set bits in binary rep of i
        dp[1] = 1
        for i in range(2, n + 1):
            if i & 1: dp[i] = dp[i//2] + 1
            else: dp[i] = dp[i//2]
        return dp