n = int(input())

cnt = 0
for _ in range(n):
  word = input()

  list = ['0']
  for i in word:
    if list[-1] == i:
      continue
    else:
      if i in list:
        break
      else:
        list.append(i)
  else:
    cnt += 1

print(cnt)