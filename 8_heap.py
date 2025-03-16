
from typing import List 
from collections import defaultdict, OrderedDict
import heapq

# 1. https://leetcode.com/problems/kth-largest-element-in-a-stream/
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap=[]
        self.size=k
        for n in nums:
            self.add(n)
        
    def add(self, val: int) -> int:
        # T:O(logk) and S:O(k)
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>self.size:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# 2. https://leetcode.com/problems/last-stone-weight/
def lastStoneWeight(stones: List[int]) -> int:
    # T:O(nlogn) and S:O(n)
    max_heap=[]
    for s in stones:
        heapq.heappush(max_heap,(-s,s))

    while len(max_heap)>1:
        top1=heapq.heappop(max_heap)[1]
        top2=heapq.heappop(max_heap)[1]
        weight=top1-top2
        if weight>0:
            heapq.heappush(max_heap,(-weight,weight))

    return max_heap[0][1] if max_heap else 0

# 3. https://leetcode.com/problems/k-closest-points-to-origin/
def kClosest( points: List[List[int]], k: int) -> List[List[int]]:
    # T:O(nlogk) and S:O(k)
    max_heap = []
    for point in points:
        distance = point[0]*point[0]+point[1]*point[1]
        heapq.heappush(max_heap,(-distance,point))
        if len(max_heap)>k:
            heapq.heappop(max_heap)
    return [point[1] for point in max_heap]

# 4. https://leetcode.com/problems/kth-largest-element-in-an-array/
def findKthLargest(self, nums: List[int], k: int) -> int:
    # T:O(nlogk) and S:O(k)
    min_heap=[]
    for num in nums:
        heapq.heappush(min_heap,num)
        if len(min_heap)>k:
            heapq.heappop(min_heap)
    return min_heap[0]

# 6. https://leetcode.com/problems/design-twitter/description/
class Twitter:

    def __init__(self):
        self.tweet_time=0
        self.following=defaultdict(set)
        self.tweets=defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        # T:O(1)
        self.tweets[userId].append((self.tweet_time,tweetId))
        self.tweet_time+=1
        

    def _merge_k_sorted_list_from_end(self,find_tweets_from_users,size=10):
        # T:O(k+size*logk)
        max_heap=[]
        latest_posts=[]
        # insert latest tweet from each user
        for user in find_tweets_from_users:
            if self.tweets[user]:
                index=len(self.tweets[user])-1
                tweet=self.tweets[user][index]
                max_heap.append((-tweet[0],tweet[1],index,user))
        # T:O(k) heapify
        heapq.heapify(max_heap)
        
        # T:O(size*logk) push and pop from heap
        while len(latest_posts)!=size and max_heap:
            top=heapq.heappop(max_heap)
            _,post,index,user=top
            latest_posts.append(post)
            if index-1>=0:
                index=index-1
                tweet=self.tweets[user][index]
                heapq.heappush(max_heap,(-tweet[0],tweet[1],index,user))
        
        return latest_posts

    def getNewsFeed(self, userId: int) -> List[int]:
        # T:O(k+size*logk)
        find_tweets_from_users=list(self.following[userId])
        find_tweets_from_users.append(userId)
        return self._merge_k_sorted_list_from_end(find_tweets_from_users)

    def follow(self, followerId: int, followeeId: int) -> None:
        # T:O(1)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # T:O(1)
        self.following[followerId].discard(followeeId)

# 7. https://leetcode.com/problems/find-median-from-data-stream/
class MedianFinder:

    def __init__(self):
        self.max_heap=[] #first half
        self.min_heap=[] #second half
        

    def addNum(self, num: int) -> None:
        # T:O(log(n)) S:O(n)
        # the below 3 lines, increases size of max_heap by 1
        heapq.heappush(self.min_heap,num)
        min_v=heapq.heappop(self.min_heap)
        heapq.heappush(self.max_heap,-min_v)

        # rebalance the heap so that size difference at max is 1
        if len(self.max_heap)-len(self.min_heap)>1:
            max_v=-heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,max_v)

    def findMedian(self) -> float:
        # T:O(log(n)) S:O(n)
        if len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        # return the average, sum of top of both heaps
        v=-self.max_heap[0]
        v+=self.min_heap[0]
        return v/2

# 