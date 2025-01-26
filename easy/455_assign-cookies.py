class Solution(object):
  def findContentChildren(self, g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    cnt = 0
    g_idx, s_idx = 0, 0
    
    g.sort()
    s.sort()

    while g_idx < len(g):
        greed = g[g_idx]
        while s_idx < len(s) and s[s_idx] < greed:
            s_idx += 1
        if s_idx >= len(s):
            return cnt
        cnt += 1
        s_idx += 1
        g_idx += 1
    return cnt        