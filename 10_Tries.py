
#1. https://leetcode.com/problems/implement-trie-prefix-tree/description/
class TrieNode:
    def __init__(self):
        self.children={}
        self.isWordEnd=False
        self.word=None # is used in 3rd problem

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
        #T:O(word_length)
        temp=self.head
        for c in word:
            if c not in temp.children:
                return False
            temp=temp.children[c]
        return temp.isWordEnd
        
    def startsWith(self, prefix: str) -> bool:
        #T:O(prefix_length)
        temp=self.head
        for c in prefix:
            if c not in temp.children:
                return False
            temp=temp.children[c]
        return True

# 2. https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
class WordDictionary:

    def __init__(self):
        self.head=TrieNode()

    def addWord(self, word: str) -> None:
        temp=self.head
        for c in word:
            if c not in temp.children:
                temp.children[c]=TrieNode()
            temp=temp.children[c]
        temp.isWordEnd=True
        
    def search(self, word: str) -> bool:
        # T: O((26^d)*(n-d)) where d is the number of '.' in word of size n
        
        def search_helper(index,node):
            # '.' means search in all chidren of the current TrieNode
            if index==len(word):
                return node.isWordEnd
            
            c=word[index]
            if c != '.':
                if c not in node.children:
                    return False
                return search_helper(index+1,node.children[c])
            else:
                for child in node.children:
                    if search_helper(index+1,node.children[child]):
                        return True
                return False
        
        return search_helper(0,self.head)

# 3. https://leetcode.com/problems/word-search-ii/description/

class WordSearch2:
    def __init__(self):
        self.head=TrieNode()
    
    def add_word(self,word):
        temp=self.head
        for c in word:
            if c not in temp.children:
                temp.children[c]=TrieNode()
            temp=temp.children[c]
        temp.isWordEnd=True
        temp.word=word
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
            Word Search: T:O(N*M*(4^L)) 
            W = Number of words, L = Average word length,  N = Rows in board,  M = Columns in board,  4^L = Worst-case DFS calls per word.
        '''
        def find_word_helper(pos_x,pos_y,node):
            char_at_pos=board[pos_x][pos_y]
            if char_at_pos not in node.children:
                return
            
            #### Forgot: to modify the node
            node=node.children[char_at_pos]
            #### I added this at the start which will fail for case: ["a"]
            if node.isWordEnd:
                ans.append(node.word)
                node.isWordEnd=False
            
            board[pos_x][pos_y]='#'
            for d in directions:
                x=pos_x+d[0]
                y=pos_y+d[1]
                if 0<=x<rows and 0<=y<cols and board[x][y]!='#':
                    find_word_helper(x,y,node)
            
            board[pos_x][pos_y]=char_at_pos
        
        #### forgot to add words to Trie
        for word in words:
            self.add_word(word)

        rows,cols=len(board),len(board[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        ans=[]
        for i in range(rows):
            for j in range(cols):
                find_word_helper(i,j,self.head)
                
        return ans
  
