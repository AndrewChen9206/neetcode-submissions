class Twitter(object):

    def __init__(self):
        self.follow_list = defaultdict(set)
        self.tweet_user = defaultdict(list)
        self.simple_timestamp = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweet_user[userId].append((self.simple_timestamp, tweetId))
        self.simple_timestamp += 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        res = []

        users = set(self.follow_list[userId])
        users.add(userId)

        for uid in users:
            if self.tweet_user[uid]:
                idx = len(self.tweet_user[uid]) - 1
                time, tweetId = self.tweet_user[uid][idx]
                heap.append((-time, tweetId, uid, idx))

        heapq.heapify(heap)

        while heap and len(res) < 10:
            neg_time, tweetId, uid, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx > 0:
                prev_time, prev_tweetId = self.tweet_user[uid][idx-1]
                heapq.heappush(heap, (-prev_time, prev_tweetId, uid, idx-1))
        
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follow_list[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)