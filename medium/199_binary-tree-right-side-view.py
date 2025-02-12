from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if root == None:
      return []

    queue = deque([root])
    right_side_vals = list()
    while queue:
      right_side_idx = len(queue) - 1
      for idx in range(len(queue)):
        node = queue.popleft()
        if idx == right_side_idx:
          right_side_vals.append(node.val)
        for child in [node.left, node.right]:
          if child == None:
            continue
          queue.append(child)

    return right_side_vals