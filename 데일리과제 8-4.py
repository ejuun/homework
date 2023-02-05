class Stack():
    def __init__(self):
        self.lst =[]

    def empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False
    
    def top(self):
        if len(self.lst) == 0:
            return None
        else:
            return self.lst[-1]
    
    def pop(self):
        if len(self.lst) == 0:
            return None
        else:
            a = self.lst.pop()
            a
            return a
    def push(self,n):
        self.lst.append(n)

    def __repr__(self):
        print(self.lst)

# s1 = Stack()
# print(s1.top())
# print(s1.pop())
# s1.push(3)
# s1.push('안녕하세요')
# print(s1.top())
# print(s1.pop())
# s1.__repr__()


# s = Stack()
# print(repr(s))
#repr 내장함수