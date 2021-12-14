from collections import deque

n, m = map(int, input().split())

array = [i for i in range(n + 1)]

condition = [[] for _ in range(n + 1)]

indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    condition[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        print(i, end=' ')

while q:
    i = q.popleft()

    for j in condition[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.append(j)
            print(j, end=' ')



