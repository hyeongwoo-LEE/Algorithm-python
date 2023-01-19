m = input()

data = []
answer = 0

for i in range(len(m)):
  if m[i] == "(":
    data.append("(")
  else:
    if m[i-1] == ")":
      data.pop()
      answer += 1
    else:
      data.pop()
      answer += len(data)


print(answer)