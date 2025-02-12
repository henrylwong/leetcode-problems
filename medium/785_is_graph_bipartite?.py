from collections import deque

class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    queue = deque([0])
    unvisited = {i for i in range(len(graph))}

    while queue or len(unvisited) > 0:
      if len(queue) == 0:
        queue.append(unvisited.pop())

      cur_nodes = set()
      for _ in range(len(queue)):
        node = queue.popleft()
        cur_nodes.add(node)

        for neigh in graph[node]:
          if neigh in cur_nodes:
            return False        
          if neigh in unvisited:
            queue.append(neigh)
            unvisited.remove(neigh)

    return True