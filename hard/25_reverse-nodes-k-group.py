# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = head
        max_length = 0
        while tmp != None:
            tmp = tmp.next
            max_length += 1

        num_groups = max_length // k
        group_cnt = 0
        
        start = ListNode(next=head)
        prev = start
        tmp = head
        while tmp != None:
            if group_cnt < num_groups:
                prev_right = prev
                left_node = tmp
                for _ in range(k):
                    next_tmp = tmp.next
                    tmp.next = prev
                    prev = tmp
                    tmp = next_tmp
                left_node.next = tmp
                prev_right.next = prev
                prev = left_node
                group_cnt += 1
            else:
                tmp = tmp.next
    
        return start.next