class MyQueue:

    def __init__(self):
        self.queue_in = []
        self.queue_out = []

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        self.peek()
        return self.queue_out.pop()

    def peek(self) -> int:
        if len(self.queue_out) == 0:
            while self.queue_in:
                self.queue_out.append(self.queue_in.pop())
        return self.queue_out[-1]

    def empty(self) -> bool:
        return len(self.queue_in) + len(self.queue_out) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()