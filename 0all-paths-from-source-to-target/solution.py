class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        target = len(graph) - 1
        def dfs(node, path):
            new_path = path.copy()
            new_path.append(node)
            if node == target:
                ans.append(new_path)
                return
            for neigh in graph[node]:
                dfs(neigh, new_path)
                
        dfs(0, [])
        return ans
