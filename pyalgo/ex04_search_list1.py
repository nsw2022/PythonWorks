# 순차 탐색
# 리스트의 첫번재 자료부터 하나씩 비교하면서 찾는 것
# 그 위치를 돌려주고(반환), 못찾으면 -1을 반환함

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            return i
    return -1

def search_list2(a, x):
    n = len(a)
    same_value = []
    for i in range(0, n):
        if a[i] == x:
            same_value.append(i)
    if len(same_value) == 0:
        return -1
    return same_value



v = [60, 5, 33, 12, 97, 24, 5]
# 매개변수 - 리스트, 찾는값
print( search_list(v, 5) )  # 1, 6
print( search_list(v, 12) ) # 3
print( search_list(v, 100) ) # -1

print(search_list2(v, 5)) # [1, 6]
print(search_list2(v, 4)) # -1
print(search_list2(v, 60)) # [0]



"""
n=len(v)
for i in range(0, n):
    if v[i] == 13:
        print("찾음")
"""



