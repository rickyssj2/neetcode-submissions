"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minrooms = 0
        conflict = 0
        start, end = sorted([i.start for i in intervals]), sorted([i.end for i in intervals])
        s, e, n = 0, 0, len(intervals)
        while s < n and e < n:
            if start[s] == end[e]:
                s += 1
                e += 1
            elif start[s] < end[e]:
                conflict += 1
                s += 1
            else:
                conflict -= 1
                e += 1
            minrooms = max(minrooms, conflict)
        return minrooms