import heapq

t = int(input())

def dijkstra(x,y):
    q = []
    heapq.heappush(q,(graph[x][y],x,y))
    distance[x][y] = graph[x][y]

    while q:
        dist,x,y = heapq.heappop(q)

        # 이미 지난 노드
        if distance[x][y] < dist:
            continue

        # 상하좌우 이동 시 좌표
        for i in range(len(direction)):
            nx = direction[i][0] + x
            ny = direction[i][1] + y

            # 그래프 벗어남
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 최단경로
            if distance[nx][ny] > dist + graph[nx][ny]:
                distance[nx][ny] = dist + graph[nx][ny]
                heapq.heappush(q,(distance[nx][ny],nx,ny))

    return distance[n-1][n-1]


for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))

    direction = [[-1,0],[1,0],[0,-1],[0,1]] #상하좌우
    INF = int(1e9)
    distance = [[INF]*n for _ in range(n)]

    print(dijkstra(0,0))
