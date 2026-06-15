from math import inf 

class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i]: miminum jumps required to reach index i (0 ≤ i < n)
        # dp[i] = min [ 1 + dp[j] (j + nums[j] ≥ i) (0 ≤ j < i) ]
        n = len(nums)
        dp = [inf] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], 1 + dp[j])
        return dp[-1]