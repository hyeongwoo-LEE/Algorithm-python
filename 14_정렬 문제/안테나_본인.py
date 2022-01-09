n = int(input())

home = list(map(int,input().split()))

result = []
for i in home:
  sum_value = 0
  for j in home:
    distance = i-j
    if distance < 0:
      sum_value += -distance
    else:
      sum_value += distance
  else:
     result.append((sum_value,i))

result.sort(key = lambda x : (x[0],x[1]))

print(result[0][1])