class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a XOR a = 0
        # a XOR 0 = a
        # A B  A^B
        # 0 0   0
        # 0 1   1
        # 1 0   1
        # 1 1   0
        # Associative
        # (A^B)^C = A^(B^C)

        s = 0
        for num in nums:
            s ^= num
        return s