from math import inf 

class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i]: miminum jumps required to reach index i (0 ≤ i < n)
        # dp[i] = min [ 1 + dp[j] (j + nums[j] ≥ i) (0 ≤ j < i) ]
        n = len(nums)
        dp = [inf] * n
        dp[0] = 0

        for i in range(n):
            for j in range(nums[i] + 1):
                dp[i + j] = min(dp[i + j], 1 + dp[i])
                if i + j == n - 1: return dp[n - 1]
        return dp[-1]