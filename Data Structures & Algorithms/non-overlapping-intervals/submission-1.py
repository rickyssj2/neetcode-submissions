from heapq import heapify, heappush, heappop

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt, ans, _ = 0, [], intervals.sort()
        ans.append(intervals[0])

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if ans[-1][1] > s:
                ans[-1][1] = min(ans[-1][1], e)
                cnt += 1
            else:
                ans.append([s, e])
        return cnt
