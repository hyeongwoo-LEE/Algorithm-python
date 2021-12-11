from itertools import combinations
import time

n,m = map(int,input().split())

array = list(map(int,input().split()))
start = time.time()
result = list((combinations(array,2)))

count = 0
for i in result:
    if i[0] == i[1]:
        continue
    count += 1

print(count)
end = time.time()

print("걸린 시간: ", end - start)