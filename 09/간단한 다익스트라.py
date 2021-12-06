import sys
input = sys.stdin.readline
INF = int(1e9)

#n=노드수, m=간선수
n,m = map(int,input().split())

start = int(input())

# 노드별 최단 거리
distance = [INF] * (n+1)

# 노드별 간선 정보
graph = [[] for _ in range(n+1)]

# 노드별 방문정보
visit = [False] * (n+1)

#모든 간선 정보 입력받기 - a=노드, b=이동노드, c=거리
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

#방문하지 않은 최단거리 노드 반환
def get_smallest_node():
  min_value = INF
  node = 0
  for i in range(1,n+1):
    if not visit[i] and distance[i] < min_value:
      min_value = distance[i]
      node = i
  return node


def dijkstra(start):
  #시작 노드 초기화
  distance[start] = 0
  visit[start] = True
  for i in graph[start]:
    distance[i[0]] = i[1]

  #시작 노드를 제외한, 노드에 대해 반복
  for _ in range(n-1):
    now = get_smallest_node()
    visit[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])