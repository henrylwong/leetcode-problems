from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def largestValues(self, root: Optional[TreeNode]) -> List[int]:        
    if root == None:
      return []

    res = list()
    queue = deque([root])
    while queue:
      max_val = None
      for _ in range(len(queue)):
        node = queue.popleft()
        if max_val == None:
          max_val = node.val
        else:
          max_val = max(max_val, node.val)

        for child in (node.left, node.right):
          if child != None:
            queue.append(child)
      assert(max_val != None)
      res.append(max_val)

    return res