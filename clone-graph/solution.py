"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.clone_nodes = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        def get_clone_node(val: int) -> 'Node':
            if val not in self.clone_nodes:
                new_node = Node(val)
                self.clone_nodes[val] = new_node
            return self.clone_nodes[val]
                 
        def dfs(node):
            if node.val in visited:
                return
            visited.add(node.val)
            clone_node = get_clone_node(node.val)
            for neigh in node.neighbors:
                new_neigh = get_clone_node(neigh.val)
                clone_node.neighbors.append(new_neigh)
                dfs(neigh)
        
        if not node:
            return None
        visited = set()
        dfs(node)
        return self.clone_nodes[node.val]
            
        
        
