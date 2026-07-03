from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sn = sum(nums)

        if abs(target) > sn:
            return 0

        width = 2 * sn + 1
        dp = [0] * width
        dp[target + sn] = 1

        for i in range(n - 1, -1, -1):
            tmp = [0] * width
            for t in range(width):
                plus = dp[t + nums[i]] if t + nums[i] < width else 0
                minus = dp[t - nums[i]] if t - nums[i] >= 0 else 0
                tmp[t] = plus + minus
            dp = tmp

        return dp[sn]  # t=0 unshifted corresponds to index sn

