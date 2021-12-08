n = int(input())

w = []
for _ in range(n):
  w.append(int(input()))

w.sort()

answer = 0
for i in range(len(w)):
  answer = max(answer, w[i]*(len(w)-i))

print(answer)