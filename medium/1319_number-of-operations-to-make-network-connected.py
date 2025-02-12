class Solution:
  def makeConnected(self, n: int, connections: List[List[int]]) -> int: 
    if len(connections) < n - 1:
      return -1

    graph = {i: list() for i in range(n)}
    for a, b in connections:
      graph[a].append(b)
      graph[b].append(a)

    res = 0
    unvisited = {i for i in range(n)}
    stack = list()
    while len(unvisited) > 0:
      if len(stack) == 0:
        stack.append(unvisited.pop())
        res += 1

      node = stack.pop()
      for neigh in graph[node]:
        if neigh not in unvisited:
            continue
        stack.append(neigh)
        unvisited.remove(neigh)
      
    return res - 1 