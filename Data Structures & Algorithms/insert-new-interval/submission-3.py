class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = [] # [[1,2], [3,5], [6,7]]
        i, n = 0, len(intervals)
        while i < n or newInterval:
            s, e = intervals[i] if i < n else [math.inf, -math.inf]
            if not newInterval or s < newInterval[0]:
                if ans and ans[-1][1] >= s:
                    ans[-1][1] = max(ans[-1][1], e)
                else:
                    ans.append([s, e])
                i += 1
            else:
                if ans and ans[-1][1] >= newInterval[0]:
                    ans[-1][1] = max(ans[-1][1], newInterval[1])
                else:
                    ans.append(newInterval)
                newInterval = None
        return ans


        # ans <- check if I overlap (I = newInterval, interval)