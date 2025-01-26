class Solution:
  def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
    M, N = len(mat), len(mat[0])

    # Populate mapping
    mapping = dict()    
    for r in range(M):
      for c in range(N):
        mapping[mat[r][c]] = (r, c)

    rows = dict()
    cols = dict() 
    # Tally r/c
    for idx in range(len(arr)):
      r, c = mapping[arr[idx]]
      rows[r] = rows.get(r, 0) + 1
      cols[c] = cols.get(c, 0) + 1

      if rows[r] == N or cols[c] == M:
        return idx
    
    return -1 # should never hit this case
        