# Student
# 클래스 생성 함수 - def __init__()
class Student:
    # 생성자 함수(멤버 함수)
    def __init__(self, name, gradle):
        self.name = name
        self.gradle = gradle
        # print(self.name, self.gradle)
    def info(self):
        print(f'이름 : {self.name}, 학년 : {self.gradle}')

    def learn(self):
        print("수업을 듣습니다.")


s1 = Student('김하나', 1)
s1.info()
s1.learn()

s2 = Student('노승우',26)
s2.info()
s2.learn()