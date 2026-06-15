from heapq import heapify, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False

        ng = n // groupSize
        freq = Counter(hand)
        minheap = list(freq.keys())
        heapify(minheap)
        
        for i in range(ng): # O(N)
            while minheap and minheap[0] not in freq:
                heappop(minheap)
    
            start = minheap[0]
            for _ in range(groupSize):
                if start not in freq: return False

                freq[start] -= 1
                if freq[start] == 0: del freq[start]
                start += 1
        return True
        