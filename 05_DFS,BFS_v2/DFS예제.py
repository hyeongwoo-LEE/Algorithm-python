def dfs(graph, start, visited):
    visited[start] = True

    print(start, end=' ')

    for i in graph[start]:

        if visited[i] != True:
            dfs(graph, i, visited)


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

dfs(graph, 1, visited)