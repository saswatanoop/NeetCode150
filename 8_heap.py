
from typing import List 
from collections import defaultdict, OrderedDict, Counter, deque
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


# 5. https://leetcode.com/problems/task-scheduler/ 
class Solution:
    # we will go cycle by cycle of size n+1, in each cycle we will try to fill the window, if we can't fill the window, we will add idle time
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # T:O(n*logk) and S:O(k) where k is the number of unique tasks
        freq=Counter(tasks)
        max_heap=[-v for v in freq.values()]
        heapq.heapify(max_heap)
        time_taken=0

        while max_heap:
            window=n+1
            rem=[]
            while window and max_heap:
                freq=heapq.heappop(max_heap)
                time_taken+=1
                freq+=1 #freq is in negative so we need to add it
                if freq:
                    rem.append(freq)
                window-=1
            if window!=0 and rem:
                time_taken+=window
                window=0
            for task in rem:
                heapq.heappush(max_heap,task)

        return time_taken
    
    def leastInterval_with_order(self, tasks: List[str], n: int) -> int:
        # This is to print the tasks as well
        # T:O(n*logk) and S:O(k) where k is the number of unique tasks
        freq=Counter(tasks)
        max_heap=[]
        pref=0 #we need preference so that if A and B have same freq, we can choose A first always
        order_of_tasks=[]
        for k,v in freq.items():
            max_heap.append((-v,pref,k)) 
            pref+=1
        heapq.heapify(max_heap)

        while max_heap:
            rem=[]
            window=n+1
            while window and max_heap:
                freq,pref,key=heapq.heappop(max_heap)
                order_of_tasks.append(key)
                freq+=1 #freq is in negative so we need to add it
                if freq:
                    rem.append((freq,pref,key))
                window-=1
            while window!=0 and rem:
                order_of_tasks.append(" ")
                window-=1
            for task in rem:
                heapq.heappush(max_heap,task)
        
        print(order_of_tasks)
        return len(order_of_tasks)


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