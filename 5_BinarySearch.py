from typing import List
from collections import defaultdict

import bisect

# bisect.bisect_left(arr, x)  -> first index where value >= x
# bisect.bisect_right(arr, x) -> first index where value > x
# x exists if i < len(arr) and arr[i] == x where i = bisect.bisect_left(arr, x)


# 1. https://leetcode.com/problems/binary-search/
def search(nums: List[int], target: int) -> int:
    # T:O(logn) and S:O(1)
    s, e = 0, len(nums) - 1

    while s <= e:
        mid = s + (e - s) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            s = mid + 1
        else:
            e = mid - 1

    return -1


# 2. https://leetcode.com/problems/search-a-2d-matrix/description/
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # T:O(logn + logm)= O(log(n*m)) and S:O(1)

    # compare with smallest and largest element in matrix first
    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False

    s, e = 0, len(matrix) - 1
    while s < e:  # when s==e we need to search in that row
        mid = s + (e - s) // 2
        row_last_value = matrix[mid][-1]
        if row_last_value == target:
            return True
        elif row_last_value < target:
            s = mid + 1
        else:
            e = mid  # it could be in same mid row, we can not remove it

    # now s==e
    pos = bisect.bisect_left(matrix[s], target)
    return pos < len(matrix[s]) and matrix[s][pos] == target


# 3. https://leetcode.com/problems/koko-eating-bananas/
def minEatingSpeed(self, piles: List[int], h: int):
    # T: O(n*log(max_pile_value)) S:O(1)

    def possible_to_eat(speed):
        time_needed = 0
        for p in piles:
            time_needed += p // speed
            time_needed += 1 if p % speed != 0 else 0
        return time_needed <= h

    # ans space in between min_speed and max_speed, use binary search
    min_speed = 1
    max_speed = max(piles)
    ans = None

    while min_speed <= max_speed:
        mid = min_speed + (max_speed - min_speed) // 2
        if possible_to_eat(mid):
            ans = mid
            max_speed = mid - 1
        else:
            min_speed = mid + 1
    return ans


# 4. https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
def findMin(self, nums: List[int]):
    # T: O(logn) S:O(1)

    s, e = 0, len(nums) - 1
    while s <= e:

        mid = s + (e - s) // 2
        if nums[s] <= nums[e]:  # Goal achieved: sorted array return leftmost
            return nums[s]

        # check mid is in which sorted subarray: and use the 1st or 2nd half accordingly
        elif nums[mid] > nums[e]:  # mid first sorted subarray
            s = mid + 1
        else:  # mid in second sorted subarray
            e = mid  # should not loose mid, don't use mid-1


# 5. https://leetcode.com/problems/search-in-rotated-sorted-array/
def search_in_rotated_array(self, nums: List[int], target: int) -> int:
    # T:O(logn) and S:O(1)

    s, e = 0, len(nums) - 1
    while s <= e:

        mid = s + (e - s) // 2
        if nums[mid] == target:  # Goal achieved: found target
            return mid

        # check mid is in which sorted subarray: and use the 1st or 2nd half accordingly
        elif nums[mid] > nums[e]:  # mid in first sorted subarray
            if nums[s] <= target < nums[mid]:
                e = mid - 1
            else:
                s = mid + 1
        else:  # mid in second sorted subarray
            if nums[mid] < target <= nums[e]:
                s = mid + 1
            else:
                e = mid - 1
        # Value is definitely not in mid index, we can remove it from search space no need for e=mid or s=mid, we can do e=mid-1 or s=mid+1

    return -1


# 6. https://leetcode.com/problems/time-based-key-value-store/description/
class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # T:O(1) and S:O(n*m) where n is number of keys and m is number of values
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int):
        # T:O(logm) and S:O(1) where m is number of values for the key
        if key not in self.store or timestamp < self.store[key][0][0]:
            return ""
        ans = None
        s, e = 0, len(self.store[key]) - 1
        while s <= e:
            mid = s + (e - s) // 2
            if self.store[key][mid][0] <= timestamp:
                ans = self.store[key][mid][1]
                s = mid + 1
            else:
                e = mid - 1
        return ans

    
    def get_using_bisect(self, key: str, timestamp: int):
        # T:O(logm) and S:O(1) where m is number of values for the key
        if key not in self.store or timestamp < self.store[key][0][0]:
            return ""
        # find list[idx][0]>timestamp so list[idx-1][0] will definitely be <=timestamp
        idx = bisect.bisect_right(self.store[key], timestamp, key=lambda x: x[0])
        return self.store[key][idx - 1][1]