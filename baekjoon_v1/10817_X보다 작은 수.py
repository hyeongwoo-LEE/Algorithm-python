n,m = map(int,input().split())

data = list(map(int,input().split()))

answer = []
for i in data:
  if i < m :
    answer.append(i)

for i in answer:
  print(i,end=" ")