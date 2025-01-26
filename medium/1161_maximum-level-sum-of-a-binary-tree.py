from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue1, queue2 = deque([root]), deque()
        max_sum, cur_sum = root.val, 0
        max_lvl, cur_lvl = 1, 1

        while queue1:
            cur_sum = 0
            while queue1:
                node = queue1.popleft()
                cur_sum += node.val

                for child in [node.left, node.right]:
                    if child != None:
                        queue2.append(child)
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_lvl = cur_lvl
            queue1 = queue2
            queue2 = deque()
            cur_lvl += 1
        
        return max_lvl
            