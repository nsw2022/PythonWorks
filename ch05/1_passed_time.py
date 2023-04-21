# 지나온 날짜 계산하기
import datetime

print(" ♠지금까지 몇일? ♠")
day1 = datetime.date(2023, 3, 16)
print(day1)

# today = datetime.date(2023, 4, 21)
today = datetime.date.today()
print(today)

passed_time = today - day1
# print(passed_time)
print("개강이후 {}일이 지났습니다.".format(passed_time.days))

