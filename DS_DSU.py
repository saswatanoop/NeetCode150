
# Dynamic DSU, works when the nodes might not be known or if nodes are not integers
class DSU:
    def __init__(self,n=None):
        self.parent = {}
        self.rank = {}
        self.component_count = 0
        
        if n:
            # nodes will be 0 to n-1
            for i in range(n):
                self.parent[i] = i
                self.rank[i] = 1
            self.component_count = n

    def find_parent(self, x):
        
        # Handles New element
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
            self.component_count += 1
        
        # Base case
        if self.parent[x] == x:
            return x
        
        # Path compression
        self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        p_x = self.find_parent(x)
        p_y = self.find_parent(y)
        # Union by rank
        if p_x != p_y:
            if self.rank[p_x] > self.rank[p_y]:
                self.rank[p_x] += self.rank[p_y]
                self.rank[p_y] = 0
                self.parent[p_y] = p_x
            else:
                self.rank[p_y] += self.rank[p_x]
                self.rank[p_x] = 0
                self.parent[p_x] = p_y
            
            # Decrease component count
            self.component_count -= 1
