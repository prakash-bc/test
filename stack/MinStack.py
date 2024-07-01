class MinStack(object):

    def __init__(self):
        self.stack = []
        self.MinStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        minVal = min(val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(minVal)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.MinStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.MinStack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()