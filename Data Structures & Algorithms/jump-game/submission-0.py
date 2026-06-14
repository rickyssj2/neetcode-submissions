class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i, num in enumerate(nums):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] |= dp[j]
        return dp[-1]