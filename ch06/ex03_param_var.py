# 문자열을 출력 하는 함수
# count -> 기본 매개 변수
# 함수 호출시 매개변수를 생략하면 기본값으로 출력됨
def print_string(text, count=1):
    for i in range(count):
        print(text)


print_string("Hello")
print_string("Hello", 2)


# 가변 매개변수 - 변수 앞에 '*'를 붙임
def calc_avg(*number):
    sum_v = 0
    for i in number:
        sum_v += i
    avg = sum_v / len(number)
    return avg


print(f'평균을 구해드립니다 : {calc_avg(10, 20, 30)}')
print(f'평균을 구해드립니다 : {calc_avg(10, 20, 30, 40)}')


# 문자열 병합하기
def merge_text(*text):
    result = ''
    for txt in text:
        result += txt
    return result


str1 = merge_text('치약', '칫솔')
str2 = merge_text('치약', '칫솔', '비누')

print(str1)
print(str2)
