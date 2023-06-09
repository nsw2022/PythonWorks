# 객체 지향 언어 - 캡슐화(정보은닉), 상속, 다형성
# Counter 클래스 만들기
# 멤버 변수에 직적 접근하지 않음 - 정보 은닉
# 함수 안에 멤버 변수를 작성
# 외부에서는 함수에 접근
class Counter:
    x = 0

    def __init__(self):
        self.x = 0
        self.x += 1


    def get_count(self):
        return Counter.x # self.x 도됨

c1 = Counter()
print(c1.x)
print(c1.get_count())  # 1

c2 = Counter()
print(c2.x)
print(c2.get_count())  # 2

c3 = Counter()
print(c3.x)
print(c3.get_count())  # 3

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