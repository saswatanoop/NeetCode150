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
1. Invert Binary Tree/Convert a Binary Tree into its Mirror Tree: https://leetcode.com/problems/invert-binary-tree/description/
2. Maximum-Depth/Height of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
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
// ============================================= Binary Search Tree ==============================================