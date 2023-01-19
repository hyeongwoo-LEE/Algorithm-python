import heapq
import sys

input = sys.stdin.readline

n = int(input())

q = []
todo = [0] * (1000+1)

for _ in range(n):
  day,value = map(int,input().split())
  heapq.heappush(q,(-value,day))

while q:
  data = heapq.heappop(q)

  for i in range(data[1],0,-1):
    if todo[i] == 0:
      todo[i] = -data[0]
      break

print(sum(todo))