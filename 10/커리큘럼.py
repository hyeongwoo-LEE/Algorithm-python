from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]

indegree = [0 for i in range(n + 1)]
cost = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    array = list(map(int, input().split()))
    j = 0
    while array[j] != -1:
        if j == 0:
            cost[i] = array[0]
        else:
            graph[array[j]].append((cost[array[j]], i))
            indegree[i] += 1
        j += 1
print(indegree)


def topology_sort():
    q = deque()
    answer = [0 for _ in range(n + 1)]
    print("graph:", graph)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    print(q)

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i[1]] -= 1
            answer[i[1]] = max(answer[i[1]], i[0])

            if indegree[i[1]] == 0:
                q.append(i[1])

    print(answer)
    print(cost)


topology_sort()