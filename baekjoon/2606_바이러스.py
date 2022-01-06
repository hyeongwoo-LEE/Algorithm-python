n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0


def dfs(start, visited):
    global answer
    visited[start] = True

    for i in graph[start]:
        if visited[i] == False:
            answer += 1
            dfs(i, visited)


dfs(1, visited)
print(answer)