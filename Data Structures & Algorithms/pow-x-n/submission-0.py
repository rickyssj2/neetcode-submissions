class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            return 1.0 / self.myPow(x, -n)
                
        if n == 0:
            return 1.0
        
        half = self.myPow(x, n // 2)
        if n & 1:
            return x * half * half
        
        return half * half