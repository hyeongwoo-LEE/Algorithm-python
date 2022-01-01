s = int(input())

count = 0
result = 0
while result <= s:
  count += 1
  result += count

if s == 1:
  print(1)
else:
  print(count-1)