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
2. Design Add and Search Words Data Structure: https://leetcode.com/problems/design-add-and-search-words-data-structure/
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
    bool serach_with_dot_in_string(string word)
    {
        return serach_with_dot_in_string_helper(word, 0, head);
    }
    // use backtracking
    bool serach_with_dot_in_string_helper(string &s, int index, TrieNode *cur)
    {
        // if no node available to search for s[index] we can't find the string s
        if (!cur)
            return false;
        // the word is present but is it a prefix of some other word or word itself is present
        if (index == s.size())
            return cur->isEnd;

        // if . we need to consider all the children nodes which might match
        if (s[index] == '.')
        {
            for (auto p : cur->children)
                if (serach_with_dot_in_string_helper(s, index + 1, p.second))
                    return true;
            return false;
        }
        // check if s[index] is present in current node and the recursively check for index+1
        return cur->children.find(s[index]) != cur->children.end() && serach_with_dot_in_string_helper(s, index + 1, cur->children[s[index]]);
    }
};

// 2
class WordDictionary
{
    Trie t;

public:
    WordDictionary()
    {
    }

    void addWord(string word)
    {
        t.insert(word);
    }

    bool search(string word)
    {
        return t.serach_with_dot_in_string(word);
    }
};
//