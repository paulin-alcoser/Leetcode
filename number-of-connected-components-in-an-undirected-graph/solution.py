class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = n
        unionFind = UnionFind(n)
        for a,b in edges:
            if unionFind.union(a,b):
                ans -= 1
        return ans
            
    
    
class UnionFind:
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1] * size
    
    def find(self, x):
        if x == self.roots[x]:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.ranks[rootX] > self.ranks[rootY]:
                self.roots[rootY] = rootX
            elif self.ranks[rootX] < self.ranks[rootY]:
                self.roots[rootX] = rootY
            else:
                self.roots[rootY] = rootX
                self.ranks[rootX] += 1
            return True
        return False
        
