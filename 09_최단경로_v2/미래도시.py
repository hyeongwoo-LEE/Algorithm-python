import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for r in range(1, n + 1):
    for u in range(1, n + 1):
        for o in range(1, n + 1):
            graph[u][o] = min(graph[u][o], graph[u][r] + graph[r][o])

cost = graph[1][k] + graph[k][x]
if cost >= INF:
    print(-1)
else:
    print(cost)