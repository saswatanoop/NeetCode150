
from typing import List 
from collections import defaultdict, OrderedDict, Counter, deque
import heapq

# 1. https://leetcode.com/problems/kth-largest-element-in-a-stream/
class KthLargest:
    
    # Pattern: min heap of size k, as k largest element 
    def __init__(self, k: int, nums: List[int]):
        self.min_heap=[] 
        self.size=k
        for n in nums:
            self.add(n)
    
    # T:O(logk) and S:O(k)
    def add(self, val: int) -> int:    
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>self.size:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# 2. https://leetcode.com/problems/last-stone-weight/
def lastStoneWeight(stones: List[int]) -> int:
    # T:O(nlogn) and S:O(n)
    
    # Pattern: max heap and how to use python's min heap as max heap
    max_heap=[(-s,s) for s in stones] # store both negative and original value to avoid confusion while popping and pushing back
    heapq.heapify(max_heap) # O(n)
    
    # n*logn 
    while len(max_heap)>1: # we need at least 2 stones to smash
        top1=heapq.heappop(max_heap)[1] #Log(n)
        top2=heapq.heappop(max_heap)[1] #Log(n) 
        weight=top1-top2
        if weight>0:
            heapq.heappush(max_heap,(-weight,weight)) #Log(n)

    return max_heap[0][1] if max_heap else 0

# 3. https://leetcode.com/problems/k-closest-points-to-origin/
def kClosest( points: List[List[int]], k: int) -> List[List[int]]:
    # T:O(nlogk) and S:O(k)
    
    # Pattern: max heap as k smallest distance and how to use python's min heap as max heap
    max_heap=[]
    for i,p in enumerate(points):
        dist=p[0]*p[0]+p[1]*p[1]
        heapq.heappush(max_heap,(-dist,i))
        if len(max_heap)>k:
            heapq.heappop(max_heap)
        
    return [points[i[1]] for i in max_heap] # Use the index stored in heap to get the point from original list

# 4. https://leetcode.com/problems/kth-largest-element-in-an-array/
def findKthLargest(self, nums: List[int], k: int) -> int:
    # T:O(nlogk) and S:O(k)
    # Pattern: min heap of size k, as kth largest element
    min_heap=[]
    for num in nums:
        heapq.heappush(min_heap,num)
        if len(min_heap)>k:
            heapq.heappop(min_heap)
    return min_heap[0]


# 5. https://leetcode.com/problems/task-scheduler/ 
class Solution:
    def leastInterval_new(self, tasks: List[str], n: int) -> int:
        # T:O(n*logk)=>O(n) as k is 26 and S:O(k) where k is the number of unique tasks
        freq = Counter(tasks)
        #freq, ord, key, if B==4, A==3 after reducing B to 3, it should be still B then A in heap for correct ordering
        max_heap = [(-count, i, task) for i, (task, count) in enumerate(freq.items())]
        heapq.heapify(max_heap) # O(k) where k is 26
        
        cycle_size = n + 1
        schedule = []

        while max_heap:

            heap_size = len(max_heap)
            # Review 1: if cycle_size=n+1 < heap size, don't pop all the heap elements, else all type of tasks will be done in this cycle
            heap_tasks_to_do_in_cur_cycle = min(heap_size, cycle_size)  
            reinsert = []

            for _ in range(heap_tasks_to_do_in_cur_cycle):
                count, i, task = heapq.heappop(max_heap)
                schedule.append(task)
                if count + 1 != 0: # Add +1 since freq is in negative
                    reinsert.append((count + 1, i, task))
            
            # Re insert in heap
            for item in reinsert:
                heapq.heappush(max_heap, item)

            # Review 2: Add idle time only if items remaining
            if max_heap:
                idle_slots = cycle_size - heap_size
                for _ in range(idle_slots):
                    schedule.append("")

        return len(schedule)
                
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

# 6. https://leetcode.com/problems/design-twitter/description/
class Twitter:

    def __init__(self):
        self.user_tweets=defaultdict(list) # userId -> list of (tweet_time,tweetId)
        self.user_follows=defaultdict(set) # userId -> set of followeeId
        self.tweet_time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # T:O(1)
        self.user_tweets[userId].append((self.tweet_time,tweetId))
        self.tweet_time+=1
    
    # Pattern: Merge K sorted lists using a heap(special case: 1) decreasing order 2) till specified size)
    def _get_latest_tweets(self,users,size=10):
        # T:O(K+ KlogU) =>O(KlogU) where K is number of tweets to retrieve and U is number of users to merge, S:O(U) for the heap

        max_heap=[]
        latest_tweets=[]

        # Create max_heap of latest tweet from all users | T:O(U) to create the heap and heapify is O(U) as well
        for userId in users:
            if self.user_tweets[userId]:
                tweet_time=self.user_tweets[userId][-1][0]
                idx=len(self.user_tweets[userId])-1
                max_heap.append((-tweet_time,idx,userId))
        heapq.heapify(max_heap)

        # Retreive merged tweets | T:O(KlogU) where K is number of tweets to retrieve and U is number of users to merge
        while len(latest_tweets)!=size and max_heap:
            _,idx,userId=heapq.heappop(max_heap)
            tweet=self.user_tweets[userId][idx][1]
            latest_tweets.append(tweet)
            idx=idx-1
            if idx>=0:
                tweet_time=self.user_tweets[userId][idx][0]
                heapq.heappush(max_heap,(-tweet_time,idx,userId))
                
        return latest_tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        # T:O(klogu) where k is number of tweets to retreive and u is number of users to merge, S:O(u) for the heap
        users=list(self.user_follows[userId])
        users.append(userId)
        return self._get_latest_tweets(users)

    def follow(self, followerId: int, followeeId: int) -> None:
        # T:O(1)
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # T:O(1)
        self.user_follows[followerId].discard(followeeId) # discard is safe to use if followeeId is not in the set, it will not raise error

# 7. https://leetcode.com/problems/find-median-from-data-stream/
class MedianFinder:

    def __init__(self):
        # we need 2 halfs, first half has max on top, second has min on top
        self.max_heap=[] # first half
        self.min_heap=[] # second half
        

    def addNum(self, num: int) -> None:
        # T:O(log(n)) S:O(n)
        # the below 3 lines, increases size of max_heap by 1
        heapq.heappush(self.min_heap,num)
        min_v=heapq.heappop(self.min_heap)
        heapq.heappush(self.max_heap,-min_v)

        # rebalance the heap so that size difference at max is 1
        if len(self.max_heap)-len(self.min_heap)==2:
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
