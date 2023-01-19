word = input()

ans = [0] * 26

for i in word:
  idx = int(ord(i) - ord('a'))
  ans[idx] = ans[idx] + 1

for i in range(26):
  print(ans[i], end= " ")