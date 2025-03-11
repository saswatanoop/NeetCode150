from typing import Optional
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
