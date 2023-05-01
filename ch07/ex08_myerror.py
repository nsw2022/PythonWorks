# 예외 미루기
# 사용하는 곳에서 발생 시킴
class Animal:
    def breathe(self):
        print("숨을 쉰다")

    def cry(self):
        raise NotImplementedError

class Dog(Animal):
    def sleep(self):
        print("강아지가 잠을 잔다")

    def cry(self):
        print("멍~ 멍~")

class Cat(Animal):
    def sleep(self):
        print("고양이가 잠을 잔다")

    # def cry(self):
    #     print("야~옹 야~옹")

dog = Dog()
dog.breathe()
dog.cry()

cat = Cat()
cat.breathe()
cat.cry()
