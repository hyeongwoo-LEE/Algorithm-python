from collections import deque

n,m = map(int,input().split())

direction = [[-1,0],[1,0],[0,-1],[0,1]] #상하좌우

graph = []
for i in range(n):
  graph.append(list(map(int,input())))

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx = x + direction[i][0]
      ny = y + direction[i][1]

      # 그래프 이탈
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      # 벽일 경우
      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
        print(queue)

  return graph[n-1][m-1]

print(bfs(0,0))