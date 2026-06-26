class MyQueue(object):

    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def fillEmptyOutStk(self):
        if not self.out_stk:
            for _ in range(len(self.in_stk)):
                self.out_stk.append(self.in_stk.pop())

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stk.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.fillEmptyOutStk()
        
        return self.out_stk.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.fillEmptyOutStk()
        
        return self.out_stk[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stk and not self.out_stk


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()