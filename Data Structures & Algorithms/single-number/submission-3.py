class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(N), O(N) using Counter
        # O(NlogN), O(N)

        # XOR: 
        # - a ^ a = 0
        # - a ^ 0 = a

        xor = 0
        for num in nums:
            xor ^= num
        return xor
