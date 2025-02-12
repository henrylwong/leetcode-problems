class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Populate graph
    graph = {i : list() for i in range(numCourses)}
    incoming = [0] * numCourses
    for prereq in prerequisites:
      u, v = prereq
      graph[v].append(u)
      incoming[u] += 1

    # Initialize stack
    stack = list()
    for i in range(numCourses):
      if incoming[i] == 0:
        stack.append(i)

    # Run topological sort
    cnt = 0
    while stack:
      cnt += 1
      course = stack.pop()
      for postreq in graph[course]:
        incoming[postreq] -= 1
        if incoming[postreq] == 0:
          stack.append(postreq)

    if cnt != numCourses:
      return False 
    return True 