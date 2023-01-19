import sys
import heapq

input = sys.stdin.readline

n = int(input())

array = list(map(int,input().split()))

q = []

for i in range(n):
  heapq.heappush(q,(array[i],i+1))

answer = []
count = 0
for _ in range(n):
  time,num = heapq.heappop(q)
  count += time
  answer.append(count)

print(sum(answer))