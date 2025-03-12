class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        ''' 
        Given that we can only modify the inner 6 cells, there are 2^6 possible cell combinations
        This would eventually result in a cycle
        '''

        mask = 0b01111110
        res = 0b0
        for idx in range(len(cells)):
            res |= cells[idx] << (len(cells) - idx - 1)
        
        
        day = 1
        cycle_start = res = ~((res << 1) ^ (res >> 1)) & mask
        cycle = [res]
        while day < n:
            res = ~((res << 1) ^ (res >> 1)) & mask
            if res == cycle_start:
                break
            cycle.append(res)
            day += 1

        res = cycle[(n - 1) % len(cycle)]
        for idx in range(len(cells)):
            cells[idx] = (res >> (len(cells) - idx - 1)) & 0b1
        
        return cells