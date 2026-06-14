from math import inf

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [inf] * len(queries)
        for i, q in enumerate(queries):
            for s, e in intervals:
                if s <= q <= e: ans[i] = min(ans[i], e - s + 1)
        return [a if a != inf else -1 for a in ans]