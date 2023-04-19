# 중첩 for문
# 5행 5열
'''
for i in range(5):
    for j in range(5):
        print('$',end='')
    print()
'''
# 스타(*) 출력
# 삼각형
'''
*
**
***
****
*****
'''


for i in range(5):
    for j in range(0,i+1):
        print('*',end='')
    print()
'''
i=0, j=0                      *
i=1, j=0 j=1                  **
i=2, j=0 j=1 j=2              ***
i=3, j=0 j=1 j=2 j=3          *****
i=1, j=0 j=1 j=2 j=3 j=4      ******
'''
for i in range(5):
    for j in range(1,6):
        print(5*i+j,end=' ') # 5는 j의 종료값
    print()
