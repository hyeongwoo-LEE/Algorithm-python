n = int(input())

data = list(map(int,input().split()))

array = []
for i in data:
  if not i in array:
    array.append(i)
  else:
    continue

array.sort()

for i in array:
  print(i, end=" ")