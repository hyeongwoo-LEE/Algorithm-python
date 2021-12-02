d = [0] * 100

def fibo(x):
    #종료 조건
    if x==1 or x==2:
        return 1
    #이미 계산한 적 있는 문제
    if d[x] != 0:
        return d[x]
    #처음 접하는 문제
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))