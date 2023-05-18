'''
아래의 출력을 보이는 프로그램을 작성해보자.
 *
 o *
 o o *
 o o o *
 o o o o *
'''

i = 1
while i <= 5:
    j = 1
    while j <= i - 1:
        print("o", end=' ')
        j += 1
    print("*")
    i += 1