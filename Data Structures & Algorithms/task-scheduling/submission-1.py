from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heapify(maxheap := [(1, -freq, key) for key, freq in Counter(tasks).items()])


        print(Counter(tasks))


        T = 1
        while maxheap:
            wakeupT, freq, taskID = heappop(maxheap)

            if wakeupT > T:
                T = wakeupT

            print(f"{T}: {taskID}")
            freq += 1
            nwakeupT = wakeupT + n + 1

            if freq != 0: heappush(maxheap, (nwakeupT, freq, taskID))

            T += 1
        
        return T - 1

        # {'A': (3, 6), 'C': 1,1, 'D': 1,1, 'E': 1,1, 'F': 1,1, 'G': 1,1}

        # 1: A
        # 2: B
        # 3: 
