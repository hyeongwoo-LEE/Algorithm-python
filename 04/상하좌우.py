n = int(input())

plan = list(input().split(' '))

x,y = 1,1
direct = [[0,-1],[0,1],[-1,0],[1,0]] #서동북남
move_type = ['L','R','U','D']

for i in range(len(plan)):
  for j in range(len(move_type)):
    if(plan[i] == move_type[j]):
      nx = x + direct[j][0]
      ny = y + direct[j][1]

  if nx <= 0 or ny <= 0 or nx > n or ny > n:
      continue

  x,y = nx,ny

print(x,y)