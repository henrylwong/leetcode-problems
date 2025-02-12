from collections import deque

class Solution:
  def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    queue = deque()
    visited = [[False, False] for i in range(n)]
    queue.append([0, None])
    visited[0] = [True, True]
    dists = [-1] * n

    redGraph = self._initGraph(n, redEdges)
    blueGraph = self._initGraph(n, blueEdges)

    dist = -1
    while queue:
      dist += 1
      for _ in range(len(queue)):
        node, prevColor = queue.popleft()
        if dists[node] == -1:
          dists[node] = dist
        if prevColor != False: # prev color was red
          for neigh in blueGraph[node]:
            if visited[neigh][1] == True:
              continue
            queue.append([neigh, False]) 
            visited[neigh][1] = True
        if prevColor != True: # prev color was blue
          for neigh in redGraph[node]:
            if visited[neigh][0] == True:
              continue
            queue.append([neigh, True]) 
            visited[neigh][0] = True
    
    return dists
  
  def _initGraph(self, n, edges):
    graph = {i: list() for i in range(n)}
    for u, v in edges:
      graph[u].append(v)
    return graph