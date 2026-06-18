class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)

        ans = [intervals[0]]

        for i in range(1, n):
            if intervals[i][0] <= ans[-1][1]:
                e1, e2 = intervals[i][1], ans[-1][1]
                ans[-1][1] = max(e1, e2)
            else:
                ans.append(intervals[i])
        
        return ans