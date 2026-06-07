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
        temp_left = self.invertTree_dfs(root.right)
        root.right = self.invertTree_dfs(root.left)
        root.left = temp_left
        return root

    def invertTree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # T:O(n) and S:O(W) where W is the width of the tree
        if not root:
            return None

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left  # swap left and right child
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
        return 1 + max(self.maxDepth_dfs(root.left), self.maxDepth_dfs(root.right))

    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        # T:O(n) and S:O(W) where W is the width of the tree
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            level += 1
            size_of_level = len(q)
            for i in range(size_of_level):
                node = q.popleft()
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

        left = compute_height(node.left)
        right = compute_height(node.right)
        self.max_diameter = max(self.max_diameter, left + right)

        return max(left, right) + 1

    self.max_diameter = 0
    compute_height(root)

    return self.max_diameter


# 4. https://leetcode.com/problems/balanced-binary-tree/


def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # T:O(n) and S:O(h) where h is the height of the tree
    # at each node of tree compute height of left and right subtree, and check if the tree is balanced

    def compute_height(node):
        if (
            not node or not self.is_balanced
        ):  # do not compute if already found unbalanced
            return 0

        left = compute_height(node.left)
        right = compute_height(node.right)

        if abs(left - right) > 1:
            self.is_balanced = False

        return max(left, right) + 1

    self.is_balanced = True
    compute_height(root)
    return self.is_balanced


# 5. and 6. https://leetcode.com/problems/same-tree/description/  https://leetcode.com/problems/subtree-of-another-tree/

class SubTreeOfAnotherTree:

    # T:O(n) and S:O(h) where h is the height of the tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        # one of the tree is empty but other one is not
        return False
    
    # T:O(n*m) and S:O(h) where h is the height of the tree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif root and subRoot:
            # Try parent node, then left subtree and right subtree
            return (
                self.isSameTree(root, subRoot)
                or self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot)
            )
        else:
            return False


# 7. https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


class LCA:

    # FOR BST: T:O(h) and S:O(1) where h is the height of the tree
    def lowestCommonAncestor_bst(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if p.val > q.val:
            return self.lowestCommonAncestor_bst(root, q, p)

        while root:
            if p.val <= root.val <= q.val:  # root is the LCA
                return root
            elif root.val < p.val:  # both p and q in right subtree
                root = root.right
            else:  # both p and q in left subtree
                root = root.left

        return None

    # T:O(n) and S:O(h) where h is the height of the tree
    def lowestCommonAncestor_btree(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        def is_any_node_found(node):
            if not node:
                return False

            at_current = False
            # Check if the current node is p or q
            if node == p or node == q:
                at_current = True

            in_left = is_any_node_found(node.left)
            in_right = is_any_node_found(node.right)

            # both nodes present in left and right subtrees, or one is at current node and other is in a subtree, set LCA
            if (in_left and in_right) or (at_current and (in_left or in_right)):
                self.lca = node

            # Return True if either of the nodes is found in the current subtree, for LCA computation in parent nodes
            return in_left or in_right or at_current

        self.lca = None
        is_any_node_found(root)  # handles case where p and q, might not be in tree
        return self.lca


# 8. https://leetcode.com/problems/binary-tree-level-order-traversal/description/


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # T:O(n) and S:O(W) where W is the width of the tree
    if not root:
        return []

    q = deque([root])  # queue for bfs, root is the first node in the queue
    lvl_order = []

    while q:
        lvl_size = len(q)
        # to store the values of nodes at the current level
        cur_lvl = [0] * lvl_size
        for i in range(lvl_size):
            node = q.popleft()
            cur_lvl[i] = node.val
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

    q = deque([root])
    right_view = []

    while q:
        lvl_size = len(q)
        for i in range(lvl_size):
            node = q.popleft()
            if i == lvl_size - 1:
                right_view.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return right_view


# 10. https://leetcode.com/problems/count-good-nodes-in-binary-tree/


def goodNodes(self, root: TreeNode) -> int:
    # T:O(n) and S:O(h) where h is the height of the tree
    def dfs(node, max_val):
        if not node:
            return
        if node.val >= max_val:
            self.count += 1
        max_val = max(max_val, node.val)
        dfs(node.left, max_val)
        dfs(node.right, max_val)

    self.count = 0
    dfs(root, float("-inf"))

    return self.count


# 11. https://leetcode.com/problems/validate-binary-search-tree/description/


def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # T: O(n) S:(h)
    # inorder: L,N,R should be in increasing order for BST

    st = []
    while root:
        st.append(root)
        root = root.left

    last = None
    while st:
        node = st.pop()  # all left processing is done, now do the node(N of LNR)
        if last and last.val >= node.val:
            return False
        last = node

        # now do the right subtree, but first add all left nodes of right subtree to stack
        node = node.right
        while node:
            st.append(node)
            node = node.left
    return True


# 12. https://leetcode.com/problems/kth-smallest-element-in-a-bst/


def kthSmallest(self, root: Optional[TreeNode], k: int):
    # T:O(n) and S:O(h) where h is the height of the tree
    st = []
    while root:
        st.append(root)
        root = root.left

    while st:
        node = st.pop()
        if (
            k == 1
        ):  # we have popped k-1 smaller elements, so the current node is the kth smallest
            return node.val
        k -= 1
        node = node.right
        while node:
            st.append(node)
            node = node.left


# 13. https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # T:O(n) and S:O(h) where h is the height of the tree
    
    def dfs(s, e): #Range of inorder traversal to consider for current subtree
        if s > e:
            return None

        # consumed index, so move the index forward for next call
        node = TreeNode(preorder[self.preorder_index])
        self.preorder_index += 1
        
        # updated s,e for left and right subtree using the position of node in inorder traversal
        index = inorder_pos[node.val]
        node.left = dfs(s, index - 1)
        node.right = dfs(index + 1, e)
        
        return node

    inorder_pos = {v: i for i, v in enumerate(inorder)} # Dictionary to store the position of each value in inorder traversal for O(1) access
    self.preorder_index = 0
    
    return dfs(0, len(preorder) - 1)


# 14. https://leetcode.com/problems/binary-tree-maximum-path-sum/description/


def maxPathSum(self, root: Optional[TreeNode]):
    # T:O(n) S:O(h) where h is the height of the tree
    
    # At each node compute, best path containing that node, and compute max path sum with that node as root
    def max_path_with_node(node):
        if not node:
            return 0

        left_path = max_path_with_node(node.left)
        right_path = max_path_with_node(node.right)

        path_with_node = max(left_path + node.val, right_path + node.val, node.val)
        self.max_path = max( 
            self.max_path, path_with_node, node.val + left_path + right_path # path with node as root, and left and right path as branches
        )

        return path_with_node

    self.max_path = float("-inf")
    max_path_with_node(root)
    return self.max_path


# 15. https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


class Codec:

    def serialize_dfs(self, root):  # use node,left and right
        # T:O(n) and S:O(h) where h is the height of the tree
        def dfs(node):
            if not node:
                preorder.append("#")
                return

            preorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        preorder = []
        dfs(root)
        return ",".join(preorder) # convert to string only when we have the complete preorder list, to avoid string concatenation at each step which is costly  

    def deserialize_dfs(self, data):
        # T:O(n) and S:O(h) where h is the height of the tree
        def dfs():
            # whenever we consume a token, we need to move the index forward, so that next time we consume the next token
            token = data[self.idx]
            self.idx += 1

            if token == "#":
                return None

            node = TreeNode(int(token))
            node.left = dfs()
            node.right = dfs()
            return node

        data = data.split(",")
        self.idx = 0
        return dfs()

    # T:O(n) and S:O(n)
    def serialize_bfs(self, root):
        if not root:
            return "#"
        q = deque([root])
        data = []
        while q:
            node = q.popleft()
            if not node:
                data.append("#")
            if node:
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(data)

    def deserialize_bfs(self, data):
        data = data.split(",")
        if data[0] == "#":
            return None

        root = TreeNode(int(data[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            # set left child and push to queue if it exists
            if data[index] != "#":
                node.left = TreeNode(int(data[index]))
                q.append(node.left)
            index += 1
            # set right child and push to queue if it exists
            if data[index] != "#":
                node.right = TreeNode(int(data[index]))
                q.append(node.right)
            index += 1

        return root

# 16. https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

    def dfs(s, e): #Range of postorder traversal to consider for current subtree
        if s > e:
            return None

        # consumed index, so move the index forward for next call
        node = TreeNode(preorder[self.preorder_index])
        self.preorder_index += 1

        # leaf node, there is left node for it to check
        if s == e:  
            return node

        # next preorder value is the root of the left subtree
        left_root_val = preorder[self.preorder_index]
        index = postorder_pos[left_root_val]  # position of left subtree root in postorder traversal

        # build left and right subtree
        node.left = dfs(s, index)
        node.right = dfs(index + 1, e - 1)  # e is the root, so don't use it

        return node

    postorder_pos = {v: i for i, v in enumerate(postorder)}
    self.preorder_index = 0

    return dfs(0, len(postorder) - 1)
