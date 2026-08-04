class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums += list(range(len(nums) + 1))
        xor = 0
        for num in nums:
            xor ^= num
        return xor