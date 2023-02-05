# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0
class Calculator():

    def add(self,x,y):
        self.x = x
        self.y = y
        return self.x + self.y
    
    def subtract(self,x,y):
        self.x = x
        self.y = y
        return self.x - self.y

    def multuply(self,x,y):
        self.x = x
        self.y = y
        return self.x * self.y

    def divide(self,x,y):
        self.x = x
        self.y = y
        try:
            return self.x / self.y
        except ZeroDivisionError:
            return '0으로 나눌 수 없습니다.'

s = Calculator()
print(s.add(1,2))
print(s.subtract(2,1))
print(s.multuply(3,4))
print(s.divide(4,0))