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
3. Word Search II: https://leetcode.com/problems/word-search-ii/description/
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

// 3
class WordSearch2
{
    TrieNode *head = new TrieNode();

    void insert(string word)
    {
        auto cur = head;
        for (auto c : word)
        {
            if (cur->children.find(c) == cur->children.end())
                cur->children[c] = new TrieNode();
            cur = cur->children[c];
        }
        cur->isEnd = true;
    }

public:
    // we will use backtracking as in word search and use trie to search for all words
    void find_words_in_grid(vector<vector<char>> &board, int i, int j, string &ans, TrieNode *cur, vector<string> &all_words)
    {
        if (i >= board.size() || j >= board[i].size() || !cur || board[i][j] == ' ')
            return;

        if (cur->children.find(board[i][j]) == cur->children.end())
            return;

        // mark the i,j as visited, go one level deeper in trie node and add c to ans string
        char c = board[i][j];
        board[i][j] = ' ';
        cur = cur->children[c];
        ans += c;

        // if the node we are at in trie is end of a word push it to list.
        if (cur->isEnd)
        {
            all_words.push_back(ans);
            cur->isEnd = false; // mark false so that same word is not pushed again, we want unique list
        }

        // go in all 4 directions
        int dx[4] = {-1, 1, 0, 0};
        int dy[4] = {0, 0, -1, 1};
        for (int k = 0; k < 4; k++)
        {
            int x = i + dx[k];
            int y = j + dy[k];
            find_words_in_grid(board, x, y, ans, cur, all_words);
        }
        // unmark the board and remove the character added for index i,j
        board[i][j] = c;
        ans.pop_back();
    }
    vector<string> findWords(vector<vector<char>> &board, vector<string> &words)
    {
        // insert in all words we want to search in trie
        for (auto word : words)
            insert(word);

        vector<string> all_words;
        string word = "";

        // use each i,j as starting for a word
        for (int i = 0; i < board.size(); i++)
            for (int j = 0; j < board[0].size(); j++)
                find_words_in_grid(board, i, j, word, head, all_words);

        return all_words;
    }
};
//