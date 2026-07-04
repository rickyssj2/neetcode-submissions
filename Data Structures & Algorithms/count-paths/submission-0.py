from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # RRRRRDD permutations?
        return factorial(m + n - 2)//(factorial(m - 1)*factorial(n - 1))