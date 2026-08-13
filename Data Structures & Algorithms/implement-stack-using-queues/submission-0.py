class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2=[]

    def push(self, x: int) -> None:
        self.q1.append(x)
        while self.q1:
            val = self.q1.pop()
            self.q2.append(val)

    def pop(self) -> int:
        return self.q2.pop()

    def top(self) -> int:
        return self.q2[-1]

    def empty(self) -> bool:
        return len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()