import sys

input = sys.stdin.readline

n = int(input())

data=[]
for _ in range(n):
  data.append(int(input()))

data.sort()

for i in data[::-1]:
  print(i)