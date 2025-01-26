import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
  def __init__(self, node):
    self.node = node
    if node != None:
      self.val = node.val
  
  def __lt__(self, other):
    return self.val < other.val

  def __repr__(self):
    return f"HeapNode({self.node})" 
  
  def _getNext(self):
    self.node = self.node.next
    if self.node != None:
      self.val = self.node.val

class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode(0, None) # build list starting from dummy
    tmp = dummy

    heap = list()
    for l in lists:
      if l == None:
        continue
      heap.append(HeapNode(l))
    heapq.heapify(heap)

    while len(heap):
      min_node = heapq.heappop(heap)
      tmp.next = min_node.node
      tmp = tmp.next 

      min_node._getNext()
      if min_node.node != None:
        heapq.heappush(heap, min_node)

    return dummy.next