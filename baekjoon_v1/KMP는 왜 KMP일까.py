data = list(input())

answer = ""
for i in data:
  if 65 <= ord(i) <= 96:
    answer += i

print(answer)

