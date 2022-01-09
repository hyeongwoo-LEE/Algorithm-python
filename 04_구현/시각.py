h = int(input())

count = 0

for i in range(h+1):
  for j in range(60):
    for z in range(60):
      result = str(i) + str(j) + str(z)
      if '3' in result:
        count += 1

print(count)