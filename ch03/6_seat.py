# 6_setas.py
# 자리배치
# 자리입장객 수, 좌석 열, 줄수

customer = int(input('입장객 수 입력 : '))
col = int(input("좌석 열 수 입력: "))

if customer % col == 0:
    row = int(customer / col)
else:
    row = int(customer / col)+1

#좌석배치
for i in range(0,row):
    for j in range(1, col+1):
        # 좌석번호가 입장객수보다 크면 빠져나옴
        num = col*i+j
        if num > customer:
            break
        print(f'좌석 : {num}', end= ' ')
    print()
