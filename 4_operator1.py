# 산술연산자 -, +, *, /, %(나머지), //(몫), 거듭제곱(**)
print('10 + 4 =', 10+4)
print('10 - 4 =', 10-4)
print('10 * 4 =', 10*4)
print('10 / 4 =', 10/4)
print('10 // 4 =', 10//4)#나머지
print('10 % 4 =', 10%4)  #몫
print('10 ** 3 =',10**3) #10x10x10
print()

# 30개의 빵을 4명이 나눠먹을 때 몫과 나머지 구하기
# 변수 - bread, people

bread = 30
people = 4

# 몫 = bread//people
몫 = int(bread/people)
나머지 = bread % people

print("빵의 갯수 :" , 몫  )
print("남은 빵의 갯수 :" , 나머지 )
print()




