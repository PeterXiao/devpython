__author__ = 'Administrator'
class PyStack:
    def _init_(self,size = 20):
        self.stack = []
        self.size = size
        self.top = -1
    def setSize(self,size):
        self.size =size
    def push(self,element):
        if self.isFull():
            raise 'PyStackOverflow'
        else:
            self.stack.append(element)
            self.top = self.top + 1
    def pop(self):
        if self.isEmpty():
            raise 'PystackUnderflow'
        else:
            element = self.stack[-1]
            self.top = self.top - 1
            del self.stack[-1]
            return element
    def Top(self):
        return self.top
    def empty(self):
        self.stack=[]
        self.top = -1
    def isEmpty(self):
        if self.top == -1:
           return True
        else:
           return False
    def isFull(self):
        if self.top == self.size-1:
            return True
        else:
            return False
#if _name_ == '_main_':
stack = PyStack()
for i in range(10):
    stack.push(i)
print(stack.top)
for i in range(10):
    print(stack.pop())
stack.empty()
for i in range(21):
    stack.push(i)








