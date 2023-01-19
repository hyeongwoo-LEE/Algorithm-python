import sys, math
from collections import deque

input = sys.stdin.readline
t = int(input())


def find_prime(prime):
    for i in range(2, int(math.sqrt(9999)) + 1):
        if prime[i] == True:
            j = 2
            while i * j < 10000:
                prime[i * j] = False
                j += 1


def bfs(start, end):
    q = deque()
    q.append((start, 0))

    visited = [False for _ in range(10000)]
    visited[start] = True

    while q:
        now, cnt = q.popleft()

        if now == end:
            return cnt

        for i in range(4):
            for j in range(10):

                num = int(str(now)[:i] + str(j) + str(now)[i + 1:])
                if prime[num] and visited[num] == False and num >= 1000:
                    visited[num] = True
                    q.append((num, cnt + 1))


prime = [True for _ in range(10000)]
find_prime(prime)

for _ in range(t):
    start, end = map(int, input().split())
    answer = bfs(start, end)
    print(answer)