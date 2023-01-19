n = int(input())

data = list(map(int,input().split()))

s = set(data)

new_data = list(s)

new_data.sort()

dic = {}

for i in range(len(new_data)):
  dic[new_data[i]] = i

answer = []

for i in data:
  answer.append(dic[i])

for i in answer:
  print(i, end=" ")