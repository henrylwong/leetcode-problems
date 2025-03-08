"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dir = dict() # node: (Node, random_val)
        
        tmp = head
        idx = 1
        while tmp != None:
            tmp.idx = idx
            tmp = tmp.next
            idx += 1
        
        tmp = head
        while tmp != None:
            random_idx = tmp.random.idx if tmp.random != None else None
            node_dir[tmp.idx] = (Node(x=tmp.val), random_idx)
            tmp = tmp.next
        
        copy_head = Node(x=0)
        prev_node = copy_head
        for node_val in node_dir:
            node, random_idx = node_dir[node_val]
            if random_idx:
                node.random = node_dir[random_idx][0]
            prev_node.next = node
            prev_node = node
        
        return copy_head.next
