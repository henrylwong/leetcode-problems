class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
    res = list()
    while stack:
      course = stack.pop()
      res.append(course)
      for postreq in graph[course]:
        incoming[postreq] -= 1
        if incoming[postreq] == 0:
          stack.append(postreq)

    if len(res) != numCourses:
      return []
    return res