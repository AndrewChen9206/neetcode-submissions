class MyStack(object):

    def __init__(self):
        self.dq = deque()
        self.top_val = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.dq.append(x)
        self.top_val = x

    def pop(self):
        """
        :rtype: int
        """
        if len(self.dq) == 1:
            return self.dq.popleft()

        for i in range(len(self.dq)-1):
            if i == len(self.dq)-2:
                self.top_val = self.dq.popleft()
                self.dq.append(self.top_val)
                break

            self.dq.append(self.dq.popleft())
        
        return self.dq.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.top_val

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.dq) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()