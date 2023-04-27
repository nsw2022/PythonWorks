from classfication.ex03_calculator import Calculator

class MoreClaculator:
    def __init__(self, x):
        self.x = x
    def cal(self,*x):
        if x==0:
            print("입력안함")
        else:
            self.x = self.x * self.x
        return self.x
    def pow(self,x,y):
        if x==0 or y == 0:
            print("0으로 나눌수 없습니다")
        else:
            a = x / y
            return a

t1 = MoreClaculator(3)
print(t1.cal())
print(t1.pow(4, 1))