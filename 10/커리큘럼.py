from collections import deque
import copy

#강의 수
n = int(input())

#간선 정보 테이블
graph = [[] for _ in range(n + 1)]

#차수 테이블
indegree = [0 for i in range(n + 1)]

#강의 시간 테이블
cost = [0 for i in range(n + 1)]

#강의 시간, 선수과목 정보 입력
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    j = 0
    while data[j] != -1:
        if j == 0:
            cost[i] = data[0]
        else:
            graph[data[j]].append(i)
            indegree[i] += 1
        j += 1



def topology_sort():
    q = deque()
    answer = copy.deepcopy(cost)

    #차수 0인 강의 큐에 추가
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            answer[i] = max(answer[i], answer[now]+cost[i])

            if indegree[i] == 0:
                q.append(i)

    for i in range(1,len(answer)):
        print(answer[i])

topology_sort()