class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.arr=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)
        if(self.min == None):
            self.min = [x]
        elif(self.min[-1]>=x):
            self.min.append(x)
            # print(self.min)

    def pop(self):
        """
        :rtype: None
        """
        
        if(self.arr[-1] == self.min[-1]):
            del self.min[-1]
        if(len(self.min)==0):
            self.min = None
        del self.arr[-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if(len(self.min )!= 0):
            return self.min[-1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()