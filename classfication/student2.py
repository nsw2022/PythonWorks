# Student
# 클래스 생성 함수 - def __init__()
class Student:
    # 생성자 함수(멤버 함수)
    def __init__(self, name, gradle):
        self.name = name
        self.gradle = gradle
        # print(self.name, self.gradle)

    # def info(self):
    #     print(f'이름 : {self.name}, 학년 : {self.gradle}')

    def __str__(self): # 멤버 정보 출력(문자형)
        return f'이름 : {self.name}, 학년 : {self.gradle}'


    def learn(self):
        print("수업을 듣습니다.")


# 메인 영역
if __name__ == "__main__":
    s1 = Student('김하나', 1)
    print(s1)
    s1.learn()

    s2 = Student('노승우', 26)
    print(s2)
    s2.learn()
