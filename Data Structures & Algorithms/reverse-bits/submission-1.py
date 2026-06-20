class Solution:
    def reverseBits(self, n: int) -> int:
        bn = bin(n)[2:]
        bn = bn.rjust(32, '0')
        bn = bn[::-1]
        return int(bn, 2)