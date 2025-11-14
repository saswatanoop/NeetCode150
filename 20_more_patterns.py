from typing import List

'''
1. Prefix Sum: for range updates
'''
# 1. Prefix Sum: for range updates
class Solution:
    # 2-D: https://leetcode.com/problems/increment-submatrices-by-one/description/    
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for row1, col1, row2, col2 in queries:
            diff[row1][col1] += 1
            diff[row2 + 1][col1] -= 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col2 + 1] += 1

        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                x1 = 0 if i == 0 else mat[i - 1][j]
                x2 = 0 if j == 0 else mat[i][j - 1]
                x3 = 0 if i == 0 or j == 0 else mat[i - 1][j - 1]
                mat[i][j] = diff[i][j] + x1 + x2 - x3
        return mat

    # 1-D: https://leetcode.com/problems/corporate-flight-bookings/description/
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        values=[0]*(n+1)
        for f1,f2,seat in bookings:
            values[f1-1]+=seat
            values[f2]-=seat
        res=[0]*n
        csum=0
        for i in range(n):
            csum+=values[i]
            res[i]=csum
        return res

    # https://leetcode.com/problems/shifting-letters-ii/description/
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        pos=[0]*(n+1)
        
        for s1,s2,d in shifts:
            delta=1 if d==1 else -1
            pos[s1]+=delta
            pos[s2+1]-=delta

        res=['']*n          
        total_shift=0
        for i in range(n):
            total_shift=(total_shift+pos[i])%26
            final_shift=(ord(s[i])-ord('a')+total_shift)%26
            new_ord=ord('a')+final_shift
            res[i]=chr(new_ord)
        
        return ''.join(res)
    
    # https://leetcode.com/problems/car-pooling/?source=submission-noac
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers=[0]*1001
        for p,d1,d2 in trips:
            passengers[d1]+=p
            passengers[d2]-=p
        csum=0
        for i in range(1001):
            csum+=passengers[i]
            if csum>capacity:
                return False
        return True
    
        