n, m = map(int, input().split())

data = []  # 맵 정보 입력 받을 리스트
temp = [[0] * m for _ in range(n)]  # 울타리를 세운 맵을 입력 받고 바이러스를 확산 시킬 맵

for _ in range(n):
    data.append(list(map(int, input().split())))

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
# 바이러스 확산
def virus(x, y):

    for i in direction:
        nx = x + i[0]
        ny = y + i[1]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)


# 안전영역 계산
def safe_size():
    safe = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1
    return safe


result = 0
# dfs
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, safe_size())
        return

    # 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)