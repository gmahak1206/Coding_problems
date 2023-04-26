class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.qu = [0]*k
        self.f = -1
        self.r = -1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.f == -1 and self.r == -1:
            self.f = 0
            self.r = 0
        else:
            self.r = (self.r + 1)% (self.size)
        self.qu[self.r] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.f == self.r:
            self.f = -1
            self.r = -1
        else:
            self.f = (self.f + 1) % self.size
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.qu[self.f]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.qu[self.r]
        

    def isEmpty(self) -> bool:
        if self.f == -1 and self.r == -1:
            return True
        return False
        

    def isFull(self) -> bool:
        if (self.r + 1 == self.f ) or (self.f == 0 and self.r == self.size-1):
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
