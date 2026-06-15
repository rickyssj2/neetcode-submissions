from math import inf 

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        jumps = 0
        n = len(nums)
        if n <= 1: return 0
        
        for i in range(n):
            rr = r
            for node in range(l, min(n, r + 1)):
                rr = max(rr, node + nums[node])
                if rr >= n - 1: return jumps + 1
            l = r + 1
            r = rr
            jumps += 1
        return -1