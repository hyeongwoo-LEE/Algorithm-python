n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or y < 0 or x > n - 1 or y > m - 1:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        # 상
        dfs(x - 1, y)
        # 하
        dfs(x + 1, y)
        # 좌
        dfs(x, y - 1)
        # 우
        dfs(x, y + 1)
        return True

    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)