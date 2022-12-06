from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        seen = set()
        
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans 
                
