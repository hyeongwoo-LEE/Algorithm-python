n = int(input())

result = 0
for _ in range(n):
  word = input()
  alpha = []
  for i in word:
    if not i in alpha:
      alpha.append(i)
    else:
      if(alpha[-1] != i):
        break
  else:
    result += 1

print(result)