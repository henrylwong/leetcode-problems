#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        assert(root != None)

        stack = list()
        cur = root
        idx = 0

        while True:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            elif len(stack) > 0: # At null Left Leaf Node
                cur = stack.pop()
                if idx == k - 1:
                    return cur.val
                idx += 1 
                cur = cur.right
            else: # Stack is empty
                break
          
        return None 