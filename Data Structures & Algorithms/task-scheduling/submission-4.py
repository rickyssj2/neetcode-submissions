from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heapify(maxheap := [(-freq, taskID) for taskID, freq in Counter(tasks).items()])

        cq = deque([])
        T = 1
        while maxheap or cq:
            while cq and cq[0][0] == T: # [(wakeupT, (freq, taskID))]
                heappush(maxheap, cq.popleft()[1])
            
            if maxheap:
                freq, taskID = heappop(maxheap)
                freq += 1
                if freq:
                    cq.append((T + n + 1, (freq, taskID)))
            elif cq:
                T = cq[0][0]
                continue
            T += 1
        return T - 1