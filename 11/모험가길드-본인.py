from collections import deque

n = int(input())
array = list(map(int, input().split()))

array.sort()

q = deque()

for i in range(len(array)):
    q.append(array[i])

count = 0
while q:

    i = q.popleft()

    j = 1
    while j < i:
        if q[0] > j + len(q):
            while q:
                q.popleft()
            break

        if q[0] > i:
            i = q[0]
            q.popleft()
            j += 1
        else:
            j += 1
            q.popleft()
    else:
        count += 1

print(count)