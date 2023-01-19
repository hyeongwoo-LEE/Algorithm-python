import sys

input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
  a, b = input().split()
  data.append((int(a),b))

data.sort(key= lambda x : x[0])

for i in data:
  print(i[0],i[1])