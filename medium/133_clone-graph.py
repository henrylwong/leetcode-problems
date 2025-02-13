"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        graph = dict()
        stack = list([node])
        visited = set()

        while stack:
            node = stack.pop()
            graph[node.val] = [Node(val=node.val, neighbors=None), [neigh.val for neigh in node.neighbors]]
            for neigh in node.neighbors:
                if neigh in visited:
                    continue
                visited.add(neigh)
                stack.append(neigh)
        
        for node_val, (node, neighbors) in graph.items():
            for neigh in neighbors:
                node.neighbors.append(graph[neigh][0])
        
        return graph[1][0]