"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        clones = {}
        def clone(node):
            if node in clones:
                return clones[node]
            clone_node = Node(node.val)
            clones[node] = clone_node
        
            for adj in node.neighbors:
                clone_node.neighbors.append(clone(adj))

            return clone_node

        
        return clone(node)


        