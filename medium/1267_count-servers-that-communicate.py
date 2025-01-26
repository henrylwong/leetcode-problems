class Solution:
  def countServers(self, grid: List[List[int]]) -> int:
    all_servers = set()
    rows = dict()
    cols = dict()
    num_servers = 0

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1: # Server found
          if i not in rows:
            rows[i] = list()
          rows[i].append((i, j))

          if j not in cols:
            cols[j] = list()
          cols[j].append((i, j))

          all_servers.add((i, j))

    for servers in rows.values():
      if len(servers) >= 2:
        for i, j in servers:
          if (i, j) not in all_servers:
            continue
          num_servers += 1
          all_servers.remove((i, j))

    for servers in cols.values():
      if len(servers) >= 2:
        for i, j in servers:
          if (i, j) not in all_servers:
            continue
          num_servers += 1
          all_servers.remove((i, j))
           
    return num_servers 
  
class Solution:
  def countServers(self, grid: List[List[int]]) -> int:
    rows = [0] * len(grid)
    cols = [0] * len(grid[0])
    all_servers = list()
    num_servers = 0

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1: # Server found
          rows[i] += 1
          cols[j] += 1
          all_servers.append((i, j))

    for i, j in all_servers:
      if rows[i] > 1 or cols[j] > 1:
        num_servers += 1
          
    return num_servers 