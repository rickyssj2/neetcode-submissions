class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # bits[i] -> how many number in nums have ith bit set
        bits = [0] * 32 # 4-byte * 32 = 128 bytes

        for num in nums:
            for i in range(32):
                if (num >> i) & 1: bits[i] += 1
        
        print(bits)

        expectation = [0] * 32
        N = len(nums) - 1
        for num in range(1, N + 1):
            for i in range(32):
                if (num >> i) & 1: expectation[i] += 1

        dup = 0
        # compare
        for i, (b, e) in enumerate(zip(bits, expectation)):
            # b = bits[i]
            # e = expectation[i]
            if e < b:
                # i know ki duplicate ith bit is set
                dup = dup | (1 << i)
        
        return dup
