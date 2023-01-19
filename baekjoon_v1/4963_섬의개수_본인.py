import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False

    if graph[x][y] == 0:
        return False

    # 북서,북,북동,동,남동,남,남서,서
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x - 1, y + 1)
        dfs(x, y + 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y - 1)
        dfs(x, y - 1)
        return True

    return False


# 북서,북,북동,동,남동,남,남서,서
direction = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                count += 1

    print(count)


