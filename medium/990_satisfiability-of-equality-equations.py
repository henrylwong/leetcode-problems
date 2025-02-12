class Solution:
  def equationsPossible(self, equations: List[str]) -> bool:
    sets = [[i] for i in range(26)]
    idxs = {i:i for i in range(26)}

    ord_a = ord('a')
    # Equality equations first
    for eq in equations:
      is_equal = eq[1] == '='
      if not is_equal:
        continue
      u, v = eq[0], eq[3]       
      u = ord(u) - ord_a
      v = ord(v) - ord_a

      if idxs[u] == idxs[v]:
        continue
      for e in sets[idxs[u]]:
        sets[idxs[v]].append(e)
        idxs[e] = idxs[v]

    # Inequality equations second
    for eq in equations:
      is_equal = eq[1] == '='
      if is_equal:
        continue
      u, v = eq[0], eq[3]       
      u = ord(u) - ord_a
      v = ord(v) - ord_a

      if idxs[u] == idxs[v]:
        return False
    return True