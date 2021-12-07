import sys
import heapq
input = sys.stdin.readline

n,m,c = map(int,input().split())

INF = int(1e9)

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

q = []
distance[c] = 0
heapq.heappush(q,(0,c))

while q:
  dist,now = heapq.heappop(q)

  if distance[now] < dist:
    continue

  for i in graph[now]:
    cost = dist + i[1]
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(q,(cost,i[0]))

count = 0
max_time = 0
for i in range(1,n+1):
  if distance[i] != INF:
    count += 1
    max_time = max(max_time, distance[i])

print(count-1,max_time)
print(distance)