import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 가는 비용 0
for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0

#간선 정보 입력받기 - 스트레이트가는 경우
for _ in range(m):
  a,b,cost = map(int,input().split())
  graph[a][b] = min(graph[a][b],cost)

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])


for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print(0,end=' ')
    else:
      print(graph[a][b], end=' ')
  print()