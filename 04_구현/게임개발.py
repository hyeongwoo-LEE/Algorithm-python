n,m = map(int, input().split())

x,y,direction = map(int, input().split())

d = [[0]*m for _ in range(n)]

d[x][y] = 1 #방문처리

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

move_type = [[-1,0],[0,1],[1,0],[0,-1]]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

turn_time = 0
count = 1

while True:
    turn_left()

    nx = x + move_type[direction][0]
    ny = y + move_type[direction][1]

    if array[nx][ny] == 0 and d[nx][ny] == 0:
        x,y = nx,ny
        count += 1
        d[nx][ny] = 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4: #4방향 모두 갈 곳이 없을 경우
        nx = x - move_type[direction][0]
        ny = y - move_type[direction][1]

        if array[nx][ny] == 1: #뒤쪽이 바다일 경우
            break

        else:
            x,y = nx,ny
            turn_time = 0


print(count)