from typing import List


class TrieNode:

    # __slots__ avoids per-object __dict__, reducing memory usage and speeding up attribute access for each object.
    # Only attributes listed in __slots__ can exist; creating new dynamic attributes raises AttributeError.
    __slots__ = ["children", "isWordEnd", "word"]

    # Use __slots__ for classes with many object instances and fixed attributes to reduce memory and improve speed.
    # Common for Trie, Tree, Linked List, Graph, and other node-based data structures.

    def __init__(self):
        self.children = {}
        self.isWordEnd = False
        self.word = None  # is used in 3rd problem


# 1. https://leetcode.com/problems/implement-trie-prefix-tree/description/
class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        # T:O(word_length)
        temp = self.head
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.isWordEnd = True

    def search(self, word: str) -> bool:
        # T:O(word_length)
        temp = self.head
        for c in word:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return temp.isWordEnd

    def delete(self, word):
        # T:O(word_length)
        def delete_helper(node, idx):
            # Base case
            if len(word) == idx:
                node.isWordEnd = False # unmark as word end
                # if no children then delete this node by returning True to parent, else return False to parent to not delete this node
                return len(node.children) == 0

            char = word[idx]
            if char not in node.children:
                return False  # Word doesn't exist in the Trie

            delete_key = delete_helper(node.children[char], idx + 1)
            if delete_key: # delete the child node, child informed parent to delete itself by returning True
                node.children.pop(char)
            
            # inform parent to delete this node if it's not a word end and has no children
            return not node.isWordEnd and len(node.children) == 0

        delete_helper(self.head, 0)

    def startsWith(self, prefix: str) -> bool:
        # T:O(prefix_length)
        temp = self.head
        for c in prefix:
            if c not in temp.children:
                return False
            temp = temp.children[c]
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
        temp.isWordEnd = True

    # Trie + DFS: T: O((26^d)*(n-d)) where d is the number of '.' in word of size n
    def search(self, word: str) -> bool:
        def search_helper(index, node):
            if index == len(word):
                return node.isWordEnd

            c = word[index]
            if c != ".":
                if c not in node.children:
                    return False
                return search_helper(index + 1, node.children[c])
            # '.' means search in all children of the current TrieNode
            else:
                for child in node.children:
                    if search_helper(index + 1, node.children[child]):
                        return True
                return False

        return search_helper(0, self.head)


# 3. https://leetcode.com/problems/word-search-ii/
class WordSearch2:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.head
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.word = word

    # Trie + DFS: T:O(N*M*(4^L)) where N = Rows in board, M = Columns in board, L = Average word length, 4^L = Worst-case DFS calls per word.
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def search_for_word(node, i, j):
            # check i, j are in range and if board[i][j] is already used
            if not (0 <= i < n and 0 <= j < m) or board[i][j] == "0":
                return

            # check if char exists in trie, only if present then continue
            char = board[i][j]
            if char not in node.children:
                return

            # mark the board pos as used
            board[i][j] = "0"
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
