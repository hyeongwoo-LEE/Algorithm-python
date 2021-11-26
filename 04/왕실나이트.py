input_data = input()

x = int(input_data[1])
y = int(ord(input_data[0]) - ord('a') + 1)


move_type =[[-2,-1],[-2,1],[2,-1],[2,1],[-1,2],[1,2],[-1,-2],[1,-2]]

count = 0

for i in range(len(move_type)):
  nx = x + move_type[i][0]
  ny = y + move_type[i][1]

  if nx < 1 or ny < 1 or nx > 8 or ny > 8:
    continue

  count += 1

print(count)