class MyQueue:

    def __init__(self):
        self.s1 = [] # primary  
        self.s2 = [] # reverse       

    def push(self, x: int) -> None:
        self.s1.append(x) # [1,2]
        self.s2 = []
        for i in range(len(self.s1)-1,-1,-1):
            self.s2.append(self.s1[i])

    def pop(self) -> int:
        val =  self.s2.pop()
        self.s1 = []
        for i in range(len(self.s2)-1,-1,-1):
            self.s1.append(self.s2[i])
        return val

    def peek(self) -> int:
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()