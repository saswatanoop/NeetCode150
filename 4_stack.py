from typing import List


# 1. https://leetcode.com/problems/valid-parentheses/description/
def isValid(self, s: str) -> bool:
    # T:O(n) and S:O(n) for stack
    valid_pairs = {"(": ")", "{": "}", "[": "]"}
    st = []
    for c in s:
        if c in valid_pairs:
            st.append(c)
        else:
            if not st or c != valid_pairs[st[-1]]:
                return False
            st.pop()
    return len(st) == 0


# 2. https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # T:O(1)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        # T:O(1)
        if self.stack[-1] == self.min_stack[-1]:
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
        if c not in ["+", "-", "*", "/"]:
            stack.append(int(c))
        else:
            second, first = stack.pop(), stack.pop()
            if c == "+":
                ans = first + second
            elif c == "-":
                ans = first - second
            elif c == "*":
                ans = first * second
            elif c == "/":
                # Mistake: ans=first//second, python truncates towards -infinity and cpp towards 0
                ans = int(first / second)
            stack.append(ans)

    return stack[0]


# 4. https://leetcode.com/problems/generate-parentheses/description/
def generateParenthesis(self, n: int) -> List[str]:
    def compute(left, right):
        if left == right == 0:
            res.append("".join(cur))
            return
        if left > 0:
            cur.append("(")
            compute(left - 1, right)
            cur.pop()
        if left < right:
            cur.append(")")
            compute(left, right - 1)
            cur.pop()

    cur = []
    res = []
    compute(n, n)
    return res


# 5. https://leetcode.com/problems/daily-temperatures/
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # T:O(n) and S:O(n) for stack
    # monotonic decreasing stack, and store index in stack
    # next greater element to the right
    n = len(temperatures)
    stack = []
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        # Mistake: temperatures[stack[-1]]<temperatures[i]
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        ans[i] = stack[-1] - i if stack else 0
        stack.append(i)
    return ans


# 6. https://leetcode.com/problems/car-fleet/
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # T:O(nlogn) and S:O(n)
    # Sort the cars based on their position, and calculate the time required to reach target,from end and not from the start.
    # first car might not reach second carbut third car can block second car, so first can reach the second and third car
    car_pos_speed = [[x, v] for x, v in zip(position, speed)]
    car_pos_speed.sort(key=lambda x: x[0], reverse=True)
    time_queue = []

    for car in car_pos_speed:
        time_required = (target - car[0]) / car[1]
        if not time_queue or time_queue[-1] < time_required:
            time_queue.append(time_required)

    return len(time_queue)


# 7. https://leetcode.com/problems/largest-rectangle-in-histogram/


def largestRectangleArea(self, heights: List[int]) -> int:
    # T:O(n) and S:O(n) for stack
    # we will compute height for each index using height[i]*(nse-pse-1)
    # nse=next smaller element position
    # pse=prev smaller element position
    st = []
    i = max_area = 0
    n = len(heights)

    while i < n or st:
        # create a stack with increasing height(same height also allowed)
        if i < n and st and heights[st[-1]] <= heights[i]:
            st.append(i)
        else:
            # we have reached end or found next smaller element for element at top of stack
            current_pos_height = heights[i] if i < n else 0
            # keep computing if current element is nse for top of stack
            while st and heights[st[-1]] >= current_pos_height:
                height_of_element_on_top_of_stack = heights[st.pop()]
                nse_pos = i
                pse_pos = st[-1] if st else -1
                area = height_of_element_on_top_of_stack * (nse_pos - pse_pos - 1)
                max_area = max(max_area, area)
            # push the current element after removing all the greater elments then it from stack
            if i < n:
                st.append(i)
        i += 1

    return max_area
