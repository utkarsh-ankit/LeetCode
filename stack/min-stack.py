class MinStack:

    def __init__(self):
        self.stack=[]
        self.mstac=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mstac:
            self.mstac.append(val)
        else:
            if val<=self.mstac[-1]:
                self.mstac.append(val)
        

    def pop(self) -> None:
        a= self.stack.pop()
        if a == self.mstac[-1]:
            self.mstac.pop()
        return a
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mstac[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()