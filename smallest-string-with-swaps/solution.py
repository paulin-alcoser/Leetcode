from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        n = len(s)
        unionFind = UnionFind(n)
        for a,b in pairs:
            unionFind.union(a,b)
        
        rootToComponent = defaultdict(list)

        for i in range(len(s)):
            root = unionFind.find(i)
            rootToComponent[root].append(i)

        for k, indices in rootToComponent.items():
            chars = []
            for i in indices:
                chars.append(s[i])
            chars = sorted(chars)

            for c, i in zip(chars, indices):
                s[i] = c

        return "".join(s)
            
        
    
class UnionFind:
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1] * size
        self.count = size
        
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
            elif self.ranks[rootX] < self.roots[rootY]:
                self.roots[rootX] = rootY
            else:
                self.roots[rootY] = rootX
                self.ranks[rootX] += 1
            self.count -= 1
    
    def num_of_groups(self):
        print(self.roots)
        print(self.count)
        return self.count
            
        
