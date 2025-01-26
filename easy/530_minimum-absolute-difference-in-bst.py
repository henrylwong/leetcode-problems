#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        tmp = root
        stack = list()
        last_num = root.val
        min_diff = None

        while True:
            if tmp:
                stack.append(tmp)
                tmp = tmp.left
            elif stack:
                tmp = stack.pop()
                diff = abs(tmp.val - last_num)
                if min_diff:
                    min_diff = min(min_diff, diff)
                else:
                    min_diff = diff
                last_num = tmp.val
                tmp = tmp.right
            else:
                break

        return min_diff