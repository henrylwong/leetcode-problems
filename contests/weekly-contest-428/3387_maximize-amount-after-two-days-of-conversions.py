from collections import deque

class Solution:
  def maxAmount(self, initialCurrency: str, pairs1: list[list[str]], rates1: list[float], pairs2: list[list[str]], rates2: list[float]) -> float:
    max_currencies = {initialCurrency: 1.0}

    # Day 1
    queue = deque([(initialCurrency, 1.0)])
    graph1 = dict()
    for idx in range(len(pairs1)):
      x, y = pairs1[idx]
      rate = rates1[idx]
      if x not in graph1:
        graph1[x] = list()
      graph1[x].append((y, rate))
      if y not in graph1:
        graph1[y] = list()
      graph1[y].append((x, 1.0 / rate))

    for _ in range(len(pairs1)):
      for _ in range(len(queue)):
        cur, val = queue.popleft()
        if cur not in graph1:
          continue
        for conv, rate in graph1[cur]: 
          new_val = rate * val
          queue.append((conv, new_val))
          max_currencies[conv] = max(new_val, max_currencies.get(conv, 0))

    # Day 2
    queue = deque()
    for cur, val in max_currencies.items():
      queue.append((cur, val))
    graph2 = dict()
    for idx in range(len(pairs2)):
      x, y = pairs2[idx]
      rate = rates2[idx]
      if x not in graph2:
        graph2[x] = list()
      graph2[x].append((y, rate))
      if y not in graph2:
        graph2[y] = list()
      graph2[y].append((x, 1.0 / rate))

    for _ in range(len(pairs2)):
      for _ in range(len(queue)):
        cur, val = queue.popleft()
        if cur not in graph2:
          continue
        for conv, rate in graph2[cur]:
          new_val = rate * val
          queue.append((conv, new_val))
          max_currencies[conv] = max(new_val, max_currencies.get(conv, 0))

    return max_currencies[initialCurrency]