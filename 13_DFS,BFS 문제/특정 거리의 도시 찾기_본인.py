from collections import deque

n, m, k, x = map(int, input().split())

# 간선 리스트 생성
graph = [[] for _ in range(n + 1)]

# 방문 테이블 생성
visited = [False] * (n + 1)

# 간선 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# bfs 사용
def bfs(graph, x, visited, k):
    visited[x] = True
    q = deque()
    q.append((0, x))
    answer = []

    while q:
        # count - 이동한 거리
        count, i = q.popleft()

        if count == k:
            answer.append(i)

        count += 1

        for j in graph[i]:
            if visited[j] == False:
                q.append((count, j))
                visited[j] = True

    if len(answer) == 0:
        print(-1)
    else:
        for i in answer:
            print(i)


bfs(graph, x, visited, k)