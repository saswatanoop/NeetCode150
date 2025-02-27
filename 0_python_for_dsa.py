# Misc
    # ASCII value
ascii_of_a= ord('a')
print(ascii_of_a)

# Algorithms in STL
'''
1. Sorting
2. Binary Search
'''

# Data Structures
'''
1. List 
2. Tuples
3. Stack
4. Deque and Queue
5. PQ/Heap
6. Set
7. Hash Map
8. Linked List
9. Binary Tree
10. Graph
11. Trie/Prefix Tree

'''
####################### Algos ######################

# Sorting
nums=[1,2,1,2,2,2,2,2]
    # Reverse
new_list_reversed = nums[::-1] #or list(reversed(nums))
reversed_nums=nums.reverse() #in-place
    # Sorting
new_sorted_list=sorted(nums)
nums.sort() # in place sort
arr = [-3, 2, -5, 1]
        # Reversed order
arr.sort(key=abs, reverse=True)
        #custom sorting logic, key parameter expects a function
nums.sort(key=lambda x: x % 10)


# Binary Search
import bisect
arr = [1, 2, 2, 3, 4, 4, 4, 5, 6]
def exists(arr, target):
    pos = bisect.bisect_left(arr, target)  # Find the leftmost position
    return pos < len(arr) and arr[pos] == target  # Check if target exists at pos

# Function to count the occurrences of a number in a sorted list
def count_occurrences(arr, target):
    left = bisect.bisect_left(arr, target)  # First position where target can be inserted
    right = bisect.bisect_right(arr, target)  # Position just after the last occurrence of target
    return right - left  # The count is the difference between the two positions

# Example usage




####################### Data structures ######################

####################################   List   ####################################

nums=[2,3,4,5,5,1,2]
nums.append(123)
size_of_nums = len(nums)
last_without_removing = nums[-1]
last_with_removing_it=nums.pop()


new_list= [0]*5     #initialize with Default value 0 of size 5
M, N = 3, 4 
matrix = [[0] * N for _ in range(M)] 
#Wrong way: matrix = [[0] * N] * M  # This creates M references to the same row!
    
#Deep copy for nested list
copy_list = nums[:] #This will create a new list as items inside it are immutable 
import copy
deep_copy_list = copy.deepcopy(matrix) 

#Iterate through list
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(fruit,index)
for fruit in fruits:
    print(fruit)
for index in range(len(fruits)):
    print(fruits[index],index)

####################################    Tuples  ####################################
# immutable and cannot add new elements to Tuple
# used as keys in dictionaries, or data in set, list can't be used in set or key in hashmap

fruits = ("apple", "banana", "cherry")
print(fruits[1]) 
for fruit in fruits:
    print(fruit)

tuple_dict={}
tuple_dict[fruits]=2

####################################   Stack    ####################################

stack = []                      #Create
stack.append(10)                #Push
popped_element = stack.pop()    #Pop
top_element = stack[-1] if stack else None #Top
size = len(stack)               #Size of Stack

####################################   Deque and Queue    ####################################
from collections import deque
dll = deque()           # Create
dll.append(10)          # Add to the right
dll.appendleft(5)       # Add to the left
dll.pop()               # Removes 10, Removes from the right
dll.popleft()           # Removes 5, Remove from the left
size = len(dll)

# View first or last element in deque
front = dll[0] if dll else None 
back = dll[-1] if dll else None 


####################################   Heap/Always min-heap    ####################################
# Python heap is always min heap, if we want to create max heap, push negative of the value
# Or we can push a tuple, where the tuple values will be used for comparision in the same order (priority1,priority2, value)

import heapq

lst = [1,5,6,12,2,5]
heapq.heapify(lst) # Convert a list into a min-heap

min_heap = [] # Initialize a Min-Heap	
heapq.heappush(min_heap, 4) # Push an element onto the heap
min_elem = min_heap[0] if min_heap else None # top value
min_elem = heapq.heappop(min_heap) # Pop from top
size=len(min_heap)

# Push a negative value to simulate a max-heap
max_heap = []
heapq.heappush(max_heap, -2)
max_elem = -heapq.heappop(max_heap) # Pop and negate the result for max-heap behavior

# Custom Priority (using tuples), (priority, value)
max_heap_2=[]
heapq.heappush(max_heap_2, (-2, 2))


####################################   Set    ####################################

s = set()                   # Empty set
s = {1, 2, 3}               # Set with values
hset2=set([1,2,3,3,3,3])    #Set from a list
s.add(4)                    # Add element to set
s.remove(2)                 # Remove (raises error if missing)
s.discard(5)                # Remove (safe, no error if missing)
exists = 3 in s             # True if 3 exists in set
s.clear()                   # Set becomes empty {}
size = len(s)               # size of set

# Iterate Over a Set
for num in s:
    print(num)  # Prints elements in any order


####################################   Hash-Map/Dictionary and Counter  ####################################

# To get freq of elements 
from collections import Counter
list_temp = [1,2,1,3,4,1]
freq_count= Counter(list_temp)


normal_dict = {}
d = {"a": 1, "b": 2}  # Dictionary with key-value pairs
d = dict(a=1, b=2)  # Another way to initialize

# Default Values with defaultdict (Avoid KeyError)
from collections import defaultdict
freq = defaultdict(int) # initialize with 0 value for all keys
default_list = defaultdict(list) # Each key will have an empty list


# Insert / Update
d["c"] = 3  # Add key "c" with value 3
d["a"] = 100  # Update key "a" to 100

# Access
value = d["b"]  # Get value of key "b" (Error if key is missing)
value = d.get("b", -1)  # Get value, return -1 if key is missing

# Delete Key
del d["a"]  # Remove key "a" (Error if missing)
value = d.pop("b")  # Remove key "b" and return its value
value = d.pop("x", "default")  # Remove key "x", return "default" if missing

exists = "c" in d  # True if key "c" exists in dictionary
size = len(d)

# Iterate Over Dictionary
for key in d:
    print(key, d[key])  # Iterate over keys

for key, value in d.items():
    print(key, value)  # Iterate over key-value pairs

for value in d.values():
    print(value)  # Iterate over values only


# Sorting Dictionary by Key and Value
sorted_dict = dict(sorted(d.items()))  # Sort by keys, we pass sorted list of (key,value) to dict
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))  # Sort by values

####################################   Linked List and Doubly-LL  ####################################
class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val  # Node value
        self.prev = prev  # Pointer to the previous node
        self.next = next  # Pointer to the next node


####################################     Binary Tree Node Class  ####################################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left child node
        self.right = right  # Right child node


####################################     Graph    ####################################
graph = defaultdict(list)
def build_graph_from_edges(edges, directed=False):
      # Use defaultdict to simplify list creation
    for u, v in edges:
        graph[u].append(v)  # Add edge u -> v
        if not directed:
            graph[v].append(u)  # Add edge v -> u for undirected graph
    return graph

####################################     Trie(Prefix Tree)   ####################################
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        temp=self.head
        for c in word:
            if c not in temp.children:
                temp.children[c]=TrieNode()
            temp=temp.children[c]
        temp.isWordEnd=True

    def search(self, word: str) -> bool:
        temp=self.head
        for c in word:
            if c not in temp.children:
                return False
            temp=temp.children[c]
        return temp.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        temp=self.head
        for c in prefix:
            if c not in temp.children:
                return False
            temp=temp.children[c]
        return True


