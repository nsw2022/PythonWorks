from classfication.ex03_calculator import Calculator

class MoreClaculator(Calculator):
    def pow(self):
        num=1
        for i in range(0, self.y):
            num = num * self.x
        return num

    def __init__(self,x,y):
        self.x = x
        self.y = y

t1 = MoreClaculator(2,4)
print(t1.pow())