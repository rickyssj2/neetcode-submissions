class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        posend = [0] * n
        negend = [0] * n
        if nums[0] > 0: posend[0] = nums[0] 
        if nums[0] <= 0: negend[0] = nums[0]

        for i in range(1, n):
            num = nums[i]
            posend[i] = max(num * posend[i - 1], num * negend[i - 1], num)
            negend[i] = min(num * negend[i - 1], num * posend[i - 1], num)
        return max(posend[i] for i in range(n)) # handle edge case