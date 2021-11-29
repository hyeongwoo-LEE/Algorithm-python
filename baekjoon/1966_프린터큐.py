from collections import deque

t = int(input())

for _ in range(t):
  n,m = map(int,input().split())
  degree = deque(list(map(int,input().split())))
  idx = deque(range(n))

  count = 0

  while degree:

    #프린트 출력
    if degree[0] == max(degree):
      degree.popleft()
      idx_result = idx.popleft()

      #출력 순서 증가
      count += 1

      #원하는 문서
      if m == idx_result:
        print(count)
        break

    #중요도가 밀린 경우
    else:
      degree.append(degree.popleft())
      idx.append(idx.popleft())