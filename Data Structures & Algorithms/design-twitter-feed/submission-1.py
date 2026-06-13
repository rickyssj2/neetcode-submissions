import time

class Twitter:

    def __init__(self):
        self.fmap = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        alltweets = self.tweets[userId].copy()
        for followeeId in self.fmap[userId]:
            alltweets.extend(self.tweets[followeeId])
        alltweets.sort(reverse=True)
        return [tweetId for _, tweetId in alltweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.fmap[followerId].add(followeeId) # O(1) idempotent

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fmap[followerId].discard(followeeId) # O(1)
        
