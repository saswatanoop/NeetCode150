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


# 5. https://leetcode.com/problems/same-tree/description/


def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # T:O(n) and S:O(h) where h is the height of the tree
    if not p and not q:
        return True
    elif p and q:
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
    else:  # one of the tree is empty but other one is not
        return False


# 6. https://leetcode.com/problems/subtree-of-another-tree/


class SubTreeOfAnotherTree:
    # T:O(n*m) and S:O(h) where h is the height of the tree
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


class Solution:

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
            # If both nodes are found in the left and right subtrees, or
            # one is at the current node and the other is in a subtree, set LCA
            if (in_left and in_right) or (at_current and (in_left or in_right)):
                self.lca = node

            # Return True if either of the nodes is found in the current subtree
            return in_left or in_right or at_current

        self.lca = None
        # handles case where p and q, might not be in tree
        is_any_node_found(root)
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


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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
    def constuct_tree(start, end):
        nonlocal index_in_preorder
        if start > end:
            return None

        value = preorder[index_in_preorder]
        node = TreeNode(value)
        index_in_preorder += 1

        node.left = constuct_tree(start, pos_in_inorder[value] - 1)
        node.right = constuct_tree(pos_in_inorder[value] + 1, end)
        return node

    pos_in_inorder = {}
    for i in range(len(inorder)):
        pos_in_inorder[inorder[i]] = i
    index_in_preorder = 0
    return constuct_tree(0, len(preorder) - 1)


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

    def serialize_dfs(self, root):
        if not root:
            return "#"

        data = (
            str(root.val)
            + ","
            + self.serialize(root.left)
            + ","
            + self.serialize(root.right)
        )
        return data

    def deserialize_dfs(self, data):
        def deserialize_helper():
            nonlocal pos
            if data[pos] == "#":
                pos += 1
                return None
            node = TreeNode(int(data[pos]))
            pos += 1
            node.left = deserialize_helper()
            node.right = deserialize_helper()
            return node

        pos = 0
        data = data.split(",")
        return deserialize_helper()
