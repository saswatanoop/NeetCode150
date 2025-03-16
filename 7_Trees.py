from typing import Optional, List
from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. https://leetcode.com/problems/invert-binary-tree/
class InvertBinaryTree:
    def invertTree_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # T:O(n) and S:O(h) where h is the height of the tree
        if not root:
            return None
        temp_left= self.invertTree(root.right)
        root.right=self.invertTree(root.left)
        root.left=temp_left
        return root
    
    def invertTree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # T:O(n) and S:O(W) where W is the width of the tree
        if not root:
            return None
        
        q=deque()
        q.append(root)

        while q:
            node=q.popleft()
            node.left,node.right=node.right,node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root

# 2. https://leetcode.com/problems/maximum-depth-of-binary-tree/
class DepthOfBinaryTree:
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        # T:O(n) and S:O(h) where h is the height of the tree
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    
    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        # T:O(n) and S:O(W) where W is the width of the tree
        q=deque()
        if root:
            q.append(root)
        
        level=0
        while q:
            level+=1
            size_of_level=len(q)
            for i in range(size_of_level):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return level

# 3. https://leetcode.com/problems/diameter-of-binary-tree/submissions/1570347919/
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # T:O(n) and S:O(h) where h is the height of the tree
    # at each node of tree compute diameter using left and right height, and store the max diameter
    def compute_height(node):
        if not node:
            return 0
        
        nonlocal max_diameter
        left=compute_height(node.left)
        right=compute_height(node.right)
        max_diameter=max(max_diameter,left+right)
        
        return max(left,right)+1
    
    max_diameter=0
    compute_height(root)
    
    return max_diameter

# 4. https://leetcode.com/problems/balanced-binary-tree/
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # T:O(n) and S:O(h) where h is the height of the tree
    # at each node of tree compute height of left and right subtree, and check if the tree is balanced
    def compute_height(node):
        if not node:
            return 0

        left=compute_height(node.left)
        right=compute_height(node.right)

        if abs(left-right)>1:
            nonlocal is_balanced
            is_balanced=False

        return max(left,right)+1  
            
    is_balanced=True
    compute_height(root)
    return is_balanced

# 5. https://leetcode.com/problems/same-tree/description/
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # T:O(n) and S:O(h) where h is the height of the tree
    if not p and not q:
        return True
    if p and q:
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
    # one of the tree is empty but other one is not
    return False
  
# 6. https://leetcode.com/problems/subtree-of-another-tree/
class SubTreeOfAnotherTree:
    # T:O(n*m) and S:O(h) where h is the height of the tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q:
            return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        # one of the tree is empty but other one is not
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) 
   
# 7. https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # T:O(n) and S:O(h) where h is the height of the tree
    def is_any_node_found(node):
        if not node:
            return False
        
        at_current=False
        # Check if the current node is p or q
        if node == p or node == q:
            at_current=True
        
        in_left=is_any_node_found(node.left)
        in_right=is_any_node_found(node.right)
        # If both nodes are found in the left and right subtrees, or
        # one is at the current node and the other is in a subtree, set LCA
        if in_left and in_right or (at_current and (in_left or in_right)):
            nonlocal lca
            lca=node
        
        # Return True if either of the nodes is found in the current subtree
        return in_left or in_right or at_current

    lca=None
    is_any_node_found(root) # handles case where p and q, might not be in tree
    return lca

# 8. https://leetcode.com/problems/binary-tree-level-order-traversal/description/
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # T:O(n) and S:O(W) where W is the width of the tree
    if not root:
        return []
    
    q=deque()
    q.append(root)
    lvl_order=[]
    
    while q:
        lvl_size=len(q)
        cur_lvl=[]
        for i in range(lvl_size):
            node=q.popleft()
            cur_lvl.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        lvl_order.append(cur_lvl)
    
    return lvl_order

# 9. https://leetcode.com/problems/binary-tree-right-side-view/description/
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    # T:O(n) and S:O(W) where W is the width of the tree
    if not root:
        return []
    q=deque()
    q.append(root)
    right_view=[]
    
    while q:
        lvl_size=len(q)
        for i in range(lvl_size):
            node=q.popleft()
            if i==lvl_size-1:
                right_view.append(node.val)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    return right_view

# 10. https://leetcode.com/problems/count-good-nodes-in-binary-tree/
def goodNodes(self, root: TreeNode) -> int:
    # T:O(n) and S:O(h) where h is the height of the tree
    def count_good_nodes(node,max_value):
        if not node:
            return 0
        count = 1 if node.val>=max_value else 0
        max_value=max(max_value,node.val)
        return count+ count_good_nodes(node.left,max_value) + count_good_nodes(node.right,max_value)
    
    return count_good_nodes(root,float("-inf"))

# 11. https://leetcode.com/problems/validate-binary-search-tree/description/
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # inorder should be sorted, LNR
    # T: O(n) S:(h)
    st=[]
    node=root
    last=None

    while st or node:
        while node:
            st.append(node)
            node=node.left
    
        node=st.pop()
        # Mistake: Was using if last: so if last was 0 the if statement was not working
        if last is not None and node.val<=last:
            return False
        last=node.val
        node =node.right
    
    return True

# 12. https://leetcode.com/problems/kth-smallest-element-in-a-bst/
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # T:O(n) and S:O(h) where h is the height of the tree
    # use inorder traversal for this
    st=[]
    node=root

    while st or node:
        while node:
            st.append(node)
            node=node.left
        k-=1
        node=st.pop()
        if k==0:
            return node.val
        node=node.right

# 13. 

# 14. https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
def maxPathSum(self, root: Optional[TreeNode]) -> int:
    # T:O(n) S:O(h) where h is the height of the tree
    # At each node compute, best path containing that node, and compute max path sum with that node as root
    def max_path(node):
        if not node:
            return 0
        left_sum=max_path(node.left)
        right_sum=max_path(node.right)
        
        best_path=max(left_sum+node.val,right_sum+node.val,node.val)
        max_path_sum= max(best_path,left_sum+right_sum+node.val)
        
        if self.ans is None or self.ans<max_path_sum:
            self.ans=max_path_sum
        
        return best_path


    self.ans=None
    max_path(root)
    return self.ans    

# 15. https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
class Codec:
    # T:O(n) and S:O(n)
    def serialize_bfs(self, root):
        if not root:
            return "#"
        q=deque([root])
        data=[]
        while q:
            node=q.popleft()
            if not node:
                data.append("#")
            if node:
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return ",".join(data)
    
    def deserialize_bfs(self, data):
        data=data.split(",")
        if data[0]=="#":
            return None

        root=TreeNode(int(data[0]))
        q=deque([root])
        index=1
        while q:
            node=q.popleft()
            # set left child and push to queue if it exists
            if data[index]!="#":
                node.left=TreeNode(int(data[index]))
                q.append(node.left)
            index+=1
            # set right child and push to queue if it exists
            if data[index]!="#":
                node.right=TreeNode(int(data[index]))
                q.append(node.right)
            index+=1

        return root
    
    
    def serialize_dfs(self, root):
        if not root:
            return "#"

        data = str(root.val)+","+self.serialize(root.left)+","+self.serialize(root.right)
        return data

    def deserialize_dfs(self, data):
        def deserialize_helper():
            nonlocal pos
            if data[pos]=="#":
                pos+=1
                return None
            node=TreeNode(int(data[pos]))
            pos+=1
            node.left=deserialize_helper()
            node.right=deserialize_helper()
            return node

        pos=0
        data=data.split(',')
        return deserialize_helper()

  