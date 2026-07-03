class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dp(i, t):
            if i == n:
                return t == target
            
            plus = dp(i + 1, t + nums[i])
            minus = dp(i + 1, t - nums[i])

            return plus + minus
        
        return dp(0, 0)