import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())

start = int(input())

INF = int(1e9)

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0

  while q:
    dist,now = heapq.heappop(q)
    # dist 가 현재 최단 거리보다 크다면 이미 들렸던 노드
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        # 노드를 거친다는 뜻
        distance[i[0]] = cost
        #현재 노드에 간선으로 연결된 노드에 들렸을 때의 총합 거리와 노드번호를 q에 푸쉬 - (총합거리,노드번호)
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])