from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def f(x):
            if x < 2: return 0

            return min(f(x-1) + cost[x-1], f(x-2) + cost[x-2])

        return f(n)
