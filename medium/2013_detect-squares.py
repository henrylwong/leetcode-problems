class DetectSquares:

    def __init__(self):
        self.points = list()
        self.hist = dict()

    def add(self, point: List[int]) -> None:
        pt_x, pt_y = point
        pt = (pt_x, pt_y)

        self.points.append(point)
        if pt not in self.hist:
            self.hist[pt] = 0
        self.hist[pt] += 1

    def count(self, point: List[int]) -> int:
        q_x, q_y = point
        res = 0
        visited = set()
        for pt_x, pt_y in self.points:
            pt = (pt_x, pt_y)
            if (pt_x, pt_y) in visited:
                continue
            visited.add(pt)
            if q_x == pt_x or q_y == pt_y:
                continue
            side_x = q_x - pt_x
            side_y = q_y - pt_y
            if abs(side_x) != abs(side_y):
                continue
            
            new_x = (q_x - side_x, q_y)
            new_y = (q_x, q_y - side_y)
            if new_x in self.hist and new_y in self.hist:
                res += self.hist[pt] * self.hist[new_x] * self.hist[new_y]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)