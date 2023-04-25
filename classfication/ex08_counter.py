# Counter 클래스 만들기

class Counter:
    x = 0

    def __init__(self):
        Counter.x += 1 # 클래스 변수

    def get_count(self):
        return Counter.x # self.x 도됨

c1 = Counter()
print(c1.get_count())  # 1

c2 = Counter()
print(c2.get_count())  # 2


'''
class Counter:
    def __init__(self):
        self.x = 0  # 인스턴스 변수
        self.x += 1 # x 1증가

    def get_count(self):
        return self.x

c1 = Counter()
print(c1.get_count()) # 1

c2 = Counter()
print(c2.get_count()) # 1
'''