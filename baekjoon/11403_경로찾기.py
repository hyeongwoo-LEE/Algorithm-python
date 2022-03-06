n = int(input())

data = []

for _ in range(n):
  data.append(list(map(int,input().split())))

for k in range(n):
  for i in range(n):
    for j in range(n):
      if data[i][j] == 1 or (data[i][k] == 1 and data[k][j]):
        data[i][j] = 1

for i in data:
  for j in i:
    print(j, end=" ")
  print()