#include <vector>
#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <list>
#include <sstream>
#include <climits>
#include <unordered_set>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
                                                       right(right) {}
};

/*
preorder and order traversal with NULL values will always be unique for each tree

Binary Tree:
1. Invert Binary Tree/Convert a Binary Tree into its Mirror Tree: https://leetcode.com/problems/invert-binary-tree/description/
2. Maximum-Depth/Height of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
3. Diameter of Binary Tree: https://leetcode.com/problems/diameter-of-binary-tree/description/
4. Balanced Binary Tree: https://leetcode.com/problems/balanced-binary-tree/description/
5. Same Tree: https://leetcode.com/problems/same-tree/description/
6. Subtree of Another Tree: https://leetcode.com/problems/subtree-of-another-tree/description/
7. Binary Tree Level Order Traversal: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
8. Binary Tree Right Side View: https://leetcode.com/problems/binary-tree-right-side-view/description/
9. Count Good Nodes in Binary Tree: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

Binary Search Tree:
1. Lowest Common Ancestor of a Binary Search Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

*/

// ============================================= Binary Tree ==============================================

// 1
class InvertBinaryTree
{
    /*
    swap left and right and recursively do the same for left and right sub trees
    T: O(n)
    S: O(height of tree) => O(n) worst case
    */
public:
    TreeNode *invertTree(TreeNode *node)
    {
        if (!node)
            return node;

        auto temp = node->right;
        node->right = invertTree(node->left);
        node->left = invertTree(temp);

        return node;
    }
};

// 2
class HeightOfBT
{
    /*
        Add 1 to height to include current node
        T: O(n)
        S: O(h)=>O(n) worst case
    */
public:
    int maxDepth(TreeNode *root)
    {
        if (!root)
            return 0;

        int left_height = maxDepth(root->left);
        int right_height = maxDepth(root->right);
        return 1 + max(left_height, right_height);
    }
};

// 3
class DiameterOfBT
{
    /*
        We will compute the diameter in each node with bottom up approach,
        the helper function returns the longest path which ends at root, which can be used by the parent node for diameter

        *IMPORTANT*
        We are computing number of nodes in diameter the problem wants edges, so it would be (no of nodes - 1)

        T:O(n)
        S:O(height) => O(n) worst case
    */

    int diameterOfBinaryTree_helper(TreeNode *root, int &diameter)
    {
        if (!root)
            return 0;

        auto left_path_length = diameterOfBinaryTree_helper(root->left, diameter);
        auto right_path_length = diameterOfBinaryTree_helper(root->right, diameter);

        diameter = max(diameter, left_path_length + right_path_length + 1);

        return 1 + max(left_path_length, right_path_length);
    }

public:
    int diameterOfBinaryTree(TreeNode *root)
    {
        int ans = 0;
        diameterOfBinaryTree_helper(root, ans);
        return ans == 0 ? 0 : ans - 1;
    }
};

// 4
class IsBalancedBT
{
    /*
        We will check if the tree is balanced in each node with bottom up approach, and return height of the subtree
        T: O(n)
        S: O(h)=>O(n) worst case
    */
    int isBalanced_helper(TreeNode *root, bool &balanced)
    {
        if (!root)
            return 0;

        int left_height = isBalanced_helper(root->left, balanced);
        int right_height = isBalanced_helper(root->right, balanced);

        if (abs(left_height - right_height) > 1)
            balanced = false;

        return 1 + max(left_height, right_height);
    }

public:
    bool isBalanced(TreeNode *root)
    {
        // all subtrees should be balanced as well
        bool balanced = true;
        isBalanced_helper(root, balanced);
        return balanced;
    }
};

// 5
bool isSameTree_helper(TreeNode *p, TreeNode *q)
{
    if (!p && !q) // both do not exist
        return true;
    if (p && q)
        return (p->val == q->val) && isSameTree_helper(p->left, q->left) &&
               isSameTree_helper(p->right, q->right);
    else // one exist and one do not
        return false;
}
class IsSameTree
{
    /*
        Check if the node values are same, then recursively check for both left
       and right subtrees T: O(n) S: O(h)=>O(n) worst case
    */
public:
    bool isSameTree(TreeNode *p, TreeNode *q)
    {
        return isSameTree_helper(p, q);
    }
};
// 6
class IsSubTree
{
    /*
        T:O(n*m) where n and m are size of each tree
        S:O(m) max height of second tree
    */
public:
    bool isSubtree(TreeNode *root, TreeNode *subRoot)
    {
        // both do not exist
        if (!root && !subRoot)
            return true;
        if (root && subRoot)
            return isSameTree_helper(root, subRoot) ||
                   isSubtree(root->left, subRoot) ||
                   isSubtree(root->right, subRoot);
        else // one exist and one do not
            return false;
    }
};

// 7
class LevelOrderTraversal
{
    /*
        T:O(n)
        S:O(max size of level)=> O(n) leaves will have n/2 nodes
    */
public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        if (!root)
            return {};
        vector<vector<int>> level_order;
        queue<TreeNode *> q;
        q.push(root);

        while (!q.empty())
        {
            int level_size = q.size();
            vector<int> level(level_size);
            for (int i = 0; i < level_size; i++)
            {
                auto temp = q.front();
                q.pop();
                level[i] = temp->val;
                if (temp->left)
                    q.push(temp->left);
                if (temp->right)
                    q.push(temp->right);
            }
            level_order.push_back(level);
        }
        return level_order;
    }
};

// 8
class RightViewOfTree
{
    /*
        Use level order traversal and store the last node of each level
        T:O(n)
        S:O(max size of level)=> O(n) leaves will have n/2 nodes
    */
public:
    vector<int> rightSideView(TreeNode *root)
    {
        if (!root)
            return {};
        vector<int> right_view;
        queue<TreeNode *> q;
        q.push(root);

        while (!q.empty())
        {
            int level_size = q.size();
            for (int i = 0; i < level_size; i++)
            {
                auto temp = q.front();
                q.pop();

                if (i == level_size - 1)
                    right_view.push_back(temp->val);

                if (temp->left)
                    q.push(temp->left);
                if (temp->right)
                    q.push(temp->right);
            }
        }
        return right_view;
    }
};

// 9
class GoodNodesInTree
{
    /*
        pass the maxValue till now to both left and right subtree and use it to compute good node
        This is top down approach
        T:O(n)
        S:O(height)=>O(n) height worst case can be n
    */
    void goodNodes_helper(TreeNode *root, int &ans, int maxValue)
    {
        if (!root)
            return;
        if (root->val >= maxValue)
            ans++;
        maxValue = max(maxValue, root->val);
        goodNodes_helper(root->left, ans, maxValue);
        goodNodes_helper(root->right, ans, maxValue);
    }

public:
    int goodNodes(TreeNode *root)
    {
        int goodCount = 0;
        goodNodes(root, goodCount, INT_MIN);
        return goodCount;
    }
};
//  ============================================= Binary Search Tree ==============================================

// 1
class LCAInBST
{
    /*
        LCA will be the node, where both p and q are divided into 2 diff subtrees
        In the problem it is given both p and q exists in tree,
        if not first check if p and q are present in tree
        T:O(logn)
        S:O(1)
    */
public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        // check first if p and q exists in tree, if not stated that p and q exists in tree
        if (p->val > q->val)
            return lowestCommonAncestor(root, q, p);

        TreeNode *temp = root;
        while (temp)
        {
            if (p->val <= temp->val && temp->val <= q->val)
                break;
            else if (temp->val > q->val)
                temp = temp->left;
            else
                temp = temp->right;
        }
        return temp;
    }
};
//