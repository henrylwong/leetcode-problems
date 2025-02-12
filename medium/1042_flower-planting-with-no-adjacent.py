from collections import deque

class Solution:
  def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
    graph = {i: list() for i in range(n)}
    for path in paths:
      u, v = path[0] - 1, path[1] - 1
      graph[u].append(v)
      graph[v].append(u)

    flowers = [-1] * n
    queue = deque([0])
    unvisited = {i for i in range(1, n)}

    while queue or len(unvisited) > 0:
      if len(queue) == 0:
        queue.append(unvisited.pop())
      node = queue.popleft()

      used_flowers = set()
      for neigh in graph[node]:
        used_flowers.add(flowers[neigh])
      for i in range(1, 5):
        if i not in used_flowers:
          flowers[node] = i
          break

      for neigh in graph[node]:
        if neigh not in unvisited:
          continue
        queue.append(neigh)
        unvisited.remove(neigh)

    return flowers
        