# 피보나치 수열 - 1 1 2 3 5 8 ...
# 첫째항 및 둘째항이 1이며, 그 뒤의 항은 바로 앞 두항의 합임

def fibo(n):
    if n <= 2: # 종료조건
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(1)) # 1
print(fibo(2)) # 1
print(fibo(3)) # 2
print(fibo(4)) # 3
print(fibo(5)) # 5
print(fibo(6)) # 8
print(fibo(7)) # 13
print(fibo(8)) # 21