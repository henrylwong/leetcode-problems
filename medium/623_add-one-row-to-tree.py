from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    '''BFS'''
    if depth == 1:
      return TreeNode(val, root, None)

    queue = deque([root])
    cur_depth = 1
    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()

        if cur_depth + 1 == depth:
          node.left = TreeNode(val, node.left, None)
          node.right = TreeNode(val, None, node.right)
        
        for child in (node.left, node.right):
          if child != None and cur_depth + 1 < depth:
            queue.append(child)
      cur_depth += 1

    return root

  def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]: 
    '''Iterative DFS'''
    if depth == 1:
      return TreeNode(val, root, None)

    stack = [(root, 1)]
    while stack:
      node, cur_depth = stack.pop()

      if cur_depth + 1 == depth:
        node.left = TreeNode(val, node.left, None)
        node.right = TreeNode(val, None, node.right)
      else:
        for child in (node.left, node.right):
          if child != None and cur_depth + 1 < depth:
            stack.append((child, cur_depth + 1))

    return root