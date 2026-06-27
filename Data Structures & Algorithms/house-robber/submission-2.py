from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i < 0: return 0
            if i == 0: return nums[0]

            return max(dp(i - 1), dp(i - 2) + nums[i])
        return dp(len(nums) - 1)