"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minrooms = 0
        minheap = [] # earliest ending meeting time
        si = sorted([(i.start, i.end) for i in intervals])
        
        for s, e in si:
            while minheap and minheap[0] <= s: heappop(minheap)
            heappush(minheap, e)
            minrooms = max(minrooms, len(minheap))
        return minrooms