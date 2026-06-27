class Solution:
    def __init__(self):
        self.memo = {0: 1, 1: 1}
    def climbStairs(self, n: int) -> int:
        # Recursion
        if n in self.memo: return self.memo[n]

        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return self.memo[n]