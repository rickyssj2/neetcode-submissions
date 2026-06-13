import time
from heapq import heappush, heappop, heapify

class Twitter:

    def __init__(self):
        self.fmap = defaultdict(set)
        self.tweets = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-time.time(), tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        alltweets = list(self.tweets[userId])
        for followeeId in self.fmap[userId]: # N = 10^7
            alltweets.extend(self.tweets[followeeId]) # M = 10
        minheap = alltweets.copy() # O(N * M) 10^8
        heapify(minheap) # O(N * M)
        ans = []
        for _ in range(min(len(minheap), 10)):
            _, tweetId = heappop(minheap) # 10logN*M
            ans.append(tweetId)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.fmap[followerId].add(followeeId) # O(1) idempotent

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fmap[followerId].discard(followeeId) # O(1)
        
