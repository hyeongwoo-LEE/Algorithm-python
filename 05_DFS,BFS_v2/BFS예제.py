from collections import deque


def bfs(graph, start, visited):
    visited[start] = True

    q = deque([start])

    while q:
        node = q.popleft()

        print(node, end=' ')

        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)


visited = [False] * 9

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

bfs(graph, 1, visited)