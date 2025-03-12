class CacheNode:
    def __init__(self, k: int, v: int, next_node = None, prev_node = None):
        self.key = k
        self.value = v
        self.next = next_node
        self.prev = prev_node

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_mapping = dict()
        self.LRU_head = CacheNode(-1, -1)
        self.MRU_head = CacheNode(-1, -1)
        self.LRU_head.next = self.MRU_head
        self.MRU_head.prev = self.LRU_head

    def get(self, key: int) -> int:
        if key not in self.node_mapping:
            return -1
        
        node = self.node_mapping[key]
        self._evict(node)
        self._makeMRU(node)

        return self.node_mapping[key].value
        
    def put(self, key: int, value: int) -> None:
        if key in self.node_mapping:
            node = self.node_mapping[key]
            node.value = value
            self._evict(node)
            self._makeMRU(node)
            return
        
        node = None
        if len(self.node_mapping) >= self.capacity: # Must evict LRU element, assumes capacity >= 1
            node = self.LRU_head.next
            self._evict(node)
            del self.node_mapping[node.key]

        # Add new node as MRU
        if node:
            node.key = key
            node.value = value
        else:
            node = CacheNode(key, value)
        self.node_mapping[key] = node
        self._makeMRU(node)
        return

    def _evict(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return
    
    def _makeMRU(self, node):
        self.MRU_head.prev.next = node
        node.prev = self.MRU_head.prev
        node.next = self.MRU_head
        self.MRU_head.prev = node
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)