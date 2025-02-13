from collections import deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = self._createGraph(edges)
        
        # Find path to root from bob
        bob_queue = deque([bob])
        bob_visited = set([bob])
        bob_parents = dict()
        while bob_queue:
            node = bob_queue.popleft()
            if node == 0:
                continue
            for neigh in graph[node]:
                if neigh in bob_visited:
                    continue
                bob_queue.append(neigh)
                bob_visited.add(neigh)
                bob_parents[neigh] = node

        # # Backtrack and mark nodes with amount at time t
        bob_path = deque([0]) # at idx t: bob is at bob_path[t] node
        bob_nodes = {}
        while bob_path[0] != bob:
            bob_path.appendleft(bob_parents[bob_path[0]])
        for idx in range(len(bob_path)):
            bob_nodes[bob_path[idx]] = idx

        # Run BFS from Alice root
        res = float('-inf')
        time_step = -1
        alice_queue = deque([(0, 0)])
        alice_visited = set([0])
        while alice_queue:
            time_step += 1
            for _ in range(len(alice_queue)):
                node, bal = alice_queue.popleft()
                # Balance update
                if node in bob_nodes and bob_nodes[node] <= time_step:
                    if bob_nodes[node] == time_step:
                        bal += amount[node] / 2
                else:
                    bal += amount[node]

                for neigh in graph[node]:
                    if neigh in alice_visited:
                        continue
                    alice_queue.append((neigh, bal))
                    alice_visited.add(neigh)
                if len(graph[node]) == 1 and node != 0:
                    res = max(res, bal)
        return int(res)

    def _createGraph(self, edges):
        graph = dict()
        for u, v in edges:
            if u not in graph:
                graph[u] = list()
            if v not in graph:
                graph[v] = list()
            graph[u].append(v)
            graph[v].append(u)
        
        return graph