

class DSU:
    def __init__(self,n=None):
        self.parent = {}
        self.rank = {}
        self.component_count = 0
        
        if n:
            for i in range(n):
                self.parent[i] = i
                self.rank[i] = 1
            self.component_count = n

    def find_parent(self, x):
        # New element:
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
            self.component_count += 1
        # Base case:
        if self.parent[x] == x:
            return x
        # Path compression
        self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find_parent(x)
        root_y = self.find_parent(y)
        # Union by rank
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
                self.rank[root_y] = 0
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]
                self.rank[root_x] = 0
            # Decrease component count
            self.component_count -= 1
