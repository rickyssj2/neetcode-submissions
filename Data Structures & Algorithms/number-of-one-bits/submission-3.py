class Solution:
    def hammingWeight(self, num: int) -> int:
        count = 0
        while num:
            num = num & (num - 1)
            count += 1
        return count