# 가위 바위 보 게임 만들기
import random


def play():
    com = ['가위', '바위', '보']
    win_list = random.choice(com)
    print(win_list)
    count = 0
    while True:
        you = input("가위바위보 중 입력해주세요: ")

        if you not in com:
            print("잘못된 입력입니다. 다시 입력해주세요")
            continue

        if you == win_list:
            print("결과: 무승부")
            count += 1
        elif (you == '가위' and win_list == '보') or (you == '바위' and win_list == '가위') or (you == '보' and win_list == '바위'):
            print("결과: 승리")
            print(f'{count}번만에 승리하셨습니다!!')
            break
        else:
            print("결과: 패")
            print("이길때 까지 한다 크킄")
            count += 1

play()