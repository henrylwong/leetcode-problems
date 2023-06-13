class SnapshotArray(object):
    SNAP_ID_IDX = 0
    VAL_IDX = 1

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.arr = [[(self.snap_id, 0)] for idx in range(length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        new_entry = (self.snap_id, val)
        if self.arr[index][-1][self.SNAP_ID_IDX] == self.snap_id:
            self.arr[index][-1] = new_entry
        else:
            self.arr[index].append(new_entry)

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        index_snaps = self.arr[index]
        
        prev_mid = None
        lo = 0
        hi = len(index_snaps) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_id = index_snaps[mid][self.SNAP_ID_IDX]

            if mid_id > snap_id:
                hi = mid - 1
            elif mid_id < snap_id:
                prev_mid = mid
                lo = mid + 1
            else:
                return index_snaps[mid][self.VAL_IDX]
        
        return index_snaps[prev_mid][self.VAL_IDX]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)