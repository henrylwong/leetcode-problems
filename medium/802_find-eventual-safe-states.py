class Solution:
  def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    rev_graph = [set() for _ in range(len(graph))]
    incoming = [0] * len(graph)
    terminal_nodes = list() 
    safe_nodes = list()

    for i in range(len(graph)):
      if len(graph[i]) == 0:
        terminal_nodes.append(i)
        safe_nodes.append(i)
      else:
        for node in graph[i]:
          rev_graph[node].add(i)
          incoming[i] += 1

    while terminal_nodes:
      idx = terminal_nodes.pop()
      for neigh in rev_graph[idx]:
        incoming[neigh] -= 1
        if incoming[neigh] == 0:
          terminal_nodes.append(neigh)
          safe_nodes.append(neigh)

    return sorted(safe_nodes)
