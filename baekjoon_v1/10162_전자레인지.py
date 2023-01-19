n = int(input())

time = [300, 60, 10]
answer = []

for i in time:
    answer.append(n//i)
    n = n%i
else:
  if n != 0:
    answer = [-1]
    print(answer[0])

if len(answer) == 3:
  print(answer[0],answer[1],answer[2])