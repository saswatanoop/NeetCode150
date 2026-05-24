
from typing import List
class TrieNode:
    
    # __slots__ avoids per-object __dict__, reducing memory usage and speeding up attribute access for each object.
    # Only attributes listed in __slots__ can exist; creating new dynamic attributes raises AttributeError.
    __slots__ = ['children', 'isWordEnd', 'word']   
    
    # Use __slots__ for classes with many object instances and fixed attributes to reduce memory and improve speed.
    # Common for Trie, Tree, Linked List, Graph, and other node-based data structures.
    
    
    def __init__(self):
        self.children={}
        self.isWordEnd=False
        self.word=None # is used in 3rd problem

#1. https://leetcode.com/problems/implement-trie-prefix-tree/description/
class Trie:

    def __init__(self):
        self.head=TrieNode()

    def insert(self, word: str) -> None:
        # T:O(word_length)
        temp=self.head
        for c in word:
            if c not in temp.children:
                temp.children[c]=TrieNode()
            temp=temp.children[c]
        temp.isWordEnd=True

    def search(self, word: str) -> bool:
        # T:O(word_length)
        temp=self.head
        for c in word:
            if c not in temp.children:
                return False
            temp=temp.children[c]
        return temp.isWordEnd
        
    def startsWith(self, prefix: str) -> bool:
        # T:O(prefix_length)
        temp=self.head
        for c in prefix:
            if c not in temp.children:
                return False
            temp=temp.children[c]
        return True

# 2. https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
class WordDictionary: 
    
    def __init__(self):
        self.head = TrieNode() 

    def addWord(self, word: str) -> None:
        temp = self.head
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.word = word
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
            Word Search: T:O(N*M*(4^L)) 
            W = Number of words, L = Average word length,  N = Rows in board,  M = Columns in board,  4^L = Worst-case DFS calls per word.
        '''
        def search_for_word(node, i, j):
            # check i, j are in range and if board[i][j] is already used
            if not (0 <= i < n and 0 <= j < m) or board[i][j] == '0':
                return
            
            # check if char exists in trie, only if present then continue
            char = board[i][j]
            if char not in node.children:
                return
            
            # mark the board pos as used
            board[i][j] = '0'
            node = node.children[char]
            
            # if word exists save it
            if node.word:
                ans.append(node.word)
                node.word = None
            
            for dx, dy in directions:
                search_for_word(node, i + dx, j + dy)

            # unmark 
            board[i][j] = char    
        
        
        # Reset the head for clean execution across multiple runs for same function
        self.head = TrieNode()
        
        n, m = len(board), len(board[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))    
        ans = [] 
        
        # add words to Trie
        for word in words: 
            self.addWord(word)
        
        # search for words in board using Trie
        for i in range(n):
            for j in range(m):
                search_for_word(self.head, i, j)
                
        return ans
