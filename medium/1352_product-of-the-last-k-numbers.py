class ProductOfNumbers:

    def __init__(self):
        self.nums = list()
        self.last_zero = -float("inf")

    def add(self, num: int) -> None:
        if len(self.nums) == 0:
            self.nums.append(num)
        elif self.nums[-1] == 0:
            self.nums.append(num)
        else:
            self.nums.append(self.nums[-1] * num)
        if self.nums[-1] == 0:
            self.last_zero = len(self.nums) - 1

    def getProduct(self, k: int) -> int:
        if k > len(self.nums):
            raise ValueError()

        if len(self.nums) - k - 1 < self.last_zero:
            return 0
        elif len(self.nums) - k - 1 == self.last_zero or k == len(self.nums):
            return self.nums[-1]
        return self.nums[-1] // self.nums[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)