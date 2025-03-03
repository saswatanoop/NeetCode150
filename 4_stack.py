
from typing import List

# 1. https://leetcode.com/problems/valid-parentheses/description/
def isValid(self, s: str) -> bool:
    # T:O(n) and S:O(n) for stack
    valid_pairs={'(':')','{':'}','[':']'}
    st=[]
    for c in s:
        if c in valid_pairs:
            st.append(c)
        else:
            if not st or c!=valid_pairs[st[-1]]:
                return False
            st.pop()
    return len(st)==0

# 2. https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        # T:O(1) 
        if not self.min_stack or self.min_stack[-1]>=val:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        # T:O(1) 
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        # T:O(1) 
        return self.stack[-1]

    def getMin(self) -> int:
        # T:O(1) 
        return self.min_stack[-1]

# 3. https://leetcode.com/problems/evaluate-reverse-polish-notation/
def evalRPN(self, tokens: List[str]) -> int:
    # T:O(n) and S:O(n) for stack
    stack = []
    for c in tokens:
        if c not in ['+','-','*','/']:
            stack.append(int(c))
        else:
            second, first = stack.pop(), stack.pop()
            if c == "+":
                ans=first+second
            elif c == "-":
                ans=first-second
            elif c == "*":
                ans=first*second
            elif c == "/":
                #Mistake: ans=first//second, python truncates towards -infinity and cpp towards 0
                ans=int(first/second)
            stack.append(ans)

    return stack[0]
    
# 5. https://leetcode.com/problems/daily-temperatures/
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # T:O(n) and S:O(n) for stack
    # monotonic decreasing stack, and store index in stack
    # next greater element to the right
    n=len(temperatures)
    stack=[]
    ans=[0]*n
    for i in range(n-1,-1,-1):
        # Mistake: temperatures[stack[-1]]<temperatures[i]
        while stack and temperatures[stack[-1]]<=temperatures[i]:
            stack.pop()
        ans[i]=stack[-1]-i if stack else 0
        stack.append(i)
    return ans

# 6. https://leetcode.com/problems/car-fleet/
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # T:O(nlogn) and S:O(n)
    # Sort the cars based on their position, and calculate the time required to reach target,from end and not from the start.
    # first car might not reach second carbut third car can block second car, so first can reach the second and third car
    car_pos_speed=[[x,v] for x,v in zip(position,speed)]
    car_pos_speed.sort(key=lambda x: x[0],reverse=True)
    time_queue=[]

    for car in car_pos_speed:
        time_required=(target-car[0])/car[1]
        if not time_queue or time_queue[-1]<time_required:
            time_queue.append(time_required)
    
    return len(time_queue)