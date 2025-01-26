#!/usr/bin/env python3

class Solution:
  '''
  Minimum diameter can be acheived by finding the node of each tree T1 and T2 that results in the minimum max height
  Merge these and return the max diameter of T1 + T2 + edge
  '''
  def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
    diameter1 = self._getDiameter(edges1)
    max_height1 = diameter1 // 2 + diameter1 % 2

    diameter2 = self._getDiameter(edges2)
    max_height2 = diameter2 // 2 + diameter2 % 2

    return max(diameter1, diameter2, max_height1 + max_height2 + 1)

  def _getAdjList(self, edges):
    adj_list = dict()
    for u, v in edges:
      for node in (u, v):
        if node not in adj_list:
          adj_list[node] = list() 
      adj_list[u].append(v)
      adj_list[v].append(u)
    return adj_list

  def _dfs(self, adj_list, start):
    dists = {start: 0}
    visited = {start}
    stack = [start]

    while stack:
      n = stack.pop()
      dist = dists[n]
      for neigh in adj_list[n]:
        if neigh not in visited:
          visited.add(neigh)
          stack.append(neigh)
          dists[neigh] = dist + 1

    max_node, max_dist = None, -1
    for node, dist in dists.items():
      if dist > max_dist:
        max_node = node
        max_dist = dist

    return max_node, max_dist
    
  def _getDiameter(self, edge_list):
    if len(edge_list) < 1:
      return 0
    adj_list = self._getAdjList(edge_list)
    rand_node = edge_list[0][0]

    max_node, max_dist = self._dfs(adj_list, rand_node)
    max_node, max_dist = self._dfs(adj_list, max_node)

    return max_dist

if __name__ == "__main__":
  cases = {
     (((0,1), (0,2), (0,3)), (((0, 1),))): 3, 
     (((0,1), (0,2), (0,3), (2,4), (2,5), (3,6), (2,7)), ((0,1), (0,2), (0,3), (2,4), (2,5), (3,6), (2,7))): 5,
     (((0,1), (2,0), (3,2), (3,6), (8,7), (4,8), (5,4), (3,5), (3,9)), ((0,1), (0,2), (0,3))): 7
  }

  soln = Solution()
  for case in cases:
    print(f"Running case: {case}")
    res = soln.minimumDiameterAfterMerge(*case)
    print(f"\tResult: {res}")
    if res == cases[case]:
        print(f"\t\033[92m\tStatus: PASS\033[0m")  
    else:
        print(f"\t\033[91m\tStatus: FAIL\033[0m")