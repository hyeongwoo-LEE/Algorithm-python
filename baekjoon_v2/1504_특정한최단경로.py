import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, v = map(int, input().split())


def dijkstra(start, end):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if end == now:
            return dist

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return INF


cost1 = dijkstra(1, u) + dijkstra(u, v) + dijkstra(v, n)
cost2 = dijkstra(1, v) + dijkstra(v, u) + dijkstra(u, n)

min_cost = min(cost1, cost2)

if min_cost >= INF:
    print(-1)
else:
    print(min_cost)