# 좌표 이동 - goto(x, y)
import random
import turtle as t
import time

t.shape("turtle")
# t.shearfactor(-0.5)
# t.shapesize(5, 5, 8) # 거북이 사이즈
# t.speed(0)

# t.up()
# time.sleep(1)
# t.goto(0, 150)
# time.sleep(1)
# t.goto(100, 150)
'''
for i in range(100):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    t.up()
    t.goto(x, y)
'''

# 마음대로 걷는 거북이
t.speed(0)
for x in range(300):
    ang = random.randint(1, 360) # 랜덤한 각도 지정
    t.setheading(ang)
    t.forward(10)

t.mainloop()