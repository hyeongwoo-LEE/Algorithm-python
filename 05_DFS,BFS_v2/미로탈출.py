from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

# 상,하.좌,우
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


bfs(0, 0)
print(graph[n - 1][m - 1])
