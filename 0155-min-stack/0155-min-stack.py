class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.min = 9999999999999

    def push(self, val: int) -> None:
        self.s1.append(val)
        if val < self.min:
            self.min = val
        self.s2.append(self.min)

    def pop(self) -> None:
        self.s1.pop()
        if not self.s1:
            self.min = 9999999999999
        if self.min == self.s2.pop():
            self.min = self.s2[-1]

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()