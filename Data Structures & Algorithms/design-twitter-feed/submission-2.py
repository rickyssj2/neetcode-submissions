import time
from heapq import heappush, heappop, heapify

class Twitter:

    def __init__(self):
        self.fmap = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        alltweets = self.tweets[userId].copy()
        for followeeId in self.fmap[userId]:
            alltweets.extend(self.tweets[followeeId])
        minheap = alltweets[:]
        heapify(minheap)
        ans = []
        for _ in range(min(len(minheap), 10)):
            _, tweetId = heappop(minheap)
            ans.append(tweetId)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.fmap[followerId].add(followeeId) # O(1) idempotent

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fmap[followerId].discard(followeeId) # O(1)
        
