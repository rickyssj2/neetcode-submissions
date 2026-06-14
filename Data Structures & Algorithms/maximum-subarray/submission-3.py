from math import inf

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # Brute Force
        # n = len(nums)
        # ans = nums[0]
        # for i in range(n):
        #     subsum = 0
        #     for j in range(i, n):
        #         subsum += nums[j]
        #         ans = max(ans, subsum)
        #         if subsum < 0: break
        # return ans

        # Kadane's Algorithm
        subsum = 0
        ans = -inf
        for num in nums:
            subsum += num
            ans = max(ans, subsum)
            if subsum < 0: subsum = 0
        return ans
