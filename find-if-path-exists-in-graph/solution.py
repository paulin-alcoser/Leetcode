class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
            
        stack = [source]
        visited = set()
        while stack:
            cur = stack.pop()
            visited.add(cur)
            if cur == destination:
                return True
            for neigh in adj_list[cur]:
                if neigh not in visited:
                    stack.append(neigh)
                    
        return False
