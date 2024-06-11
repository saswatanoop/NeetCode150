#include <vector>
#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
#include <map>
#include <string>
#include <algorithm>
#include <list>
#include <sstream>
#include <climits>
#include <unordered_set>

using namespace std;

/*
1. Implement Trie (Prefix Tree): https://leetcode.com/problems/implement-trie-prefix-tree/description/
2.
*/

// 1
class TrieNode
{
public:
    // map and unordered_map are fine, since we know 26 chars will be there log26 is constant
    map<char, TrieNode *> children;
    bool isEnd = false;
};
class Trie
{
    TrieNode *head;

public:
    Trie()
    {
        head = new TrieNode();
    }

    void insert(string word)
    {
        auto cur = head;
        for (auto c : word)
        {
            // create the character node if it does not exist
            if (cur->children.find(c) == cur->children.end())
                cur->children[c] = new TrieNode();
            cur = cur->children[c];
        }
        // to show at this character a word ends
        cur->isEnd = true;
    }

    bool search(string word)
    {
        auto cur = head;
        for (auto c : word)
        {
            if (cur->children.find(c) == cur->children.end())
                return false;
            cur = cur->children[c];
        }
        // check if any word ends at this node
        return cur->isEnd;
    }

    bool startsWith(string prefix)
    {
        auto cur = head;
        for (auto c : prefix)
        {
            if (cur->children.find(c) == cur->children.end())
                return false;
            cur = cur->children[c];
        }
        return true;
    }
};

//