from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        incoming = {i: 0 for i in range(len(graph))}
        paths = {i: list() for i in range(len(graph))}
        queue = deque([0])
        paths[0].append([0])
        res = list()

        for u in range(len(graph)):
            for v in graph[u]:
                incoming[v] += 1
        if incoming[0] != 0:
            return []  
            
        while queue:
            node = queue.popleft()
            for neigh in graph[node]:
                for path in paths[node]:
                    new_path = path + [neigh]
                    paths[neigh].append(new_path)
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    queue.append(neigh)
        return paths[len(graph) - 1]