class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
        visited = set()
        def dfs(node):
            visited.add(node)
            if node == destination:
                return True
            for neigh in adj_list[node]:
                if neigh not in visited:
                    found_destination = dfs(neigh)
                    if found_destination:
                        return True
            return False
        return dfs(source)
