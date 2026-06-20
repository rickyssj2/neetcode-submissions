class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            ans ^= num ^ (i + 1)
        return ans