from math import inf
from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(intervals), len(queries)
        intervals.sort()
        sq = sorted([(q, i) for i, q in enumerate(queries)])
        ans = [-1] * m
        i = 0
        minheap = []
        for q, qi in sq:

            # Add all intervals into the heap in which i lie
            while i < n:
                s, e = intervals[i]
                if q < s:
                    break
                heappush(minheap, (e - s + 1, i))
                i += 1
                
            while minheap and intervals[minheap[0][1]][1] < q: heappop(minheap)

            if minheap: ans[qi] = minheap[0][0]
        return ans

