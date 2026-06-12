from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskmap = {}
        for k, v in Counter(tasks).items():
            taskmap[k] = [0, v]
        # print(taskmap)
        T = 1
        while taskmap:
            # Find ready task with max freq
            maxf = 0
            taskID = ""
            for k, (w, f) in taskmap.items():
                if w <= T and f > maxf:
                    taskID = k
                    maxf = f
            # Assign
            if taskID:
                taskmap[taskID][0] = T + n + 1
                taskmap[taskID][1] -= 1
                if not taskmap[taskID][1]: del taskmap[taskID]
            T += 1
        return T - 1