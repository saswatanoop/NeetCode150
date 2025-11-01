from typing import List

'''
XOR properties:
Commutative: A^B= B^A
Associative: (A^B)^C = A^(B^C)
Identity: A^0 = A
Negation: A^A = 0

Bit Manipulation Tricks:
1. Check if ith bit is set: (n & (1 << i)) !=
2. Set ith bit: n | (1 << i)
3. Clear ith bit: n & ~(1 << i)
4. Toggle ith bit: n ^ (1 << i)
6. Get rightmost(MSB) set bit: n & -n
7. Clear LSB: n=n&(n-1)
'''

# 1.  Single Number
# https://leetcode.com/problems/single-number/
def singleNumber(nums: List[int]) -> int:
    # T: O(n), S: O(1)
    unique=0
    for n in nums:
        unique^=n #XORing same number results in 0, thus all duplicates will cancel out, Negation: A^A=0 
    return unique


# 2. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
def hammingWeight(n: int) -> int:
    # T: O(k), S: O(1), k is number of 1 bits in n
    count_of_one_bits = 0
    while n:
        n=n&(n-1) #Clear LSB: n=n&(n-1)
        count_of_one_bits+=1
    return count_of_one_bits
        
# 3. Counting Bits
# https://leetcode.com/problems/counting-bits/
def countBits(self, n: int) -> List[int]:
    # T: O(n), S: O(1): excluding output array
    dp=[0]*(n+1)
    for i in range(n+1):
        dp[i]=dp[i//2]+(i&1)
    return dp

# 4. Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/
def reverseBits(n: int) -> int:
    # T: O(1), S: O(1)
    reversed_n=0
    for i in range(32):
        if n & (1<<i):
            reversed_n=reversed_n|(1<<(31-i))
    return reversed_n

# 5. Missing Number:
# https://leetcode.com/problems/missing-number/description/
def missingNumber(self, nums: List[int]) -> int:
    # T: O(n), S: O(1) 
    n=len(nums)
    missing=0
    for i in range(1,n+1):
        missing^=(nums[i-1]^i)
    return missing

# 6. Sum of Two Integers    
# https://leetcode.com/problems/sum-of-two-integers/
def getSum(self, a: int, b: int) -> int:
    # T: O(1), S: O(1)
    MASK=0xFFFFFFFF
    MAX_INT=0x7FFFFFFF

    while b:
        carry=((a&b)<<1) & MASK
        a=(a^b)& MASK
        b=carry
    
    return a if a<=MAX_INT else ~(a^MASK)
'''
In Cpp:
    int getSum(int a, int b) {
        
        while(b)
        {
            int carry=(a&b)<<1;
            a=a^b;
            b=carry;
        }
        return a;
    }
'''

# 7. Reverse integer
# https://leetcode.com/problems/reverse-integer/description/
def reverse(self, x: int) -> int:
    # T: O(1), S: O(1)
    num=abs(x)
    reversed_num=0
    while num:
        rem=num%10
        reversed_num=reversed_num*10+rem
        num=num//10

    reversed_num=reversed_num if x>0 else -reversed_num
    reversed_num = reversed_num if (-2**31)<=reversed_num<=(2**31-1) else 0
    return reversed_num
