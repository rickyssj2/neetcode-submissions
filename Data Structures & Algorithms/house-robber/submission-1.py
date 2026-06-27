class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        b = c = nums[0]

        for i in range(1, n):
            c = max(b, nums[i] + a)
            a, b = b, c

        return c