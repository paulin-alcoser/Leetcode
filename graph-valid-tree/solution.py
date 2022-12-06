class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        unionFind = UnionFind(n)
        num_of_graphs = n
        for a,b in edges:
            if unionFind.union(a,b):
                num_of_graphs -= 1
            else:
                return False
                
        return num_of_graphs == 1
            
        
        
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.ranks = [1] * size
        
    def find(self, x) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.ranks[rootX] > self.ranks[rootY]:
                self.root[rootY] = rootX
            elif self.ranks[rootX] < self.ranks[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.ranks[rootX] += 1
            return True
        return False
