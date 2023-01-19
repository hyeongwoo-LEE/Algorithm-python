import sys

input = sys.stdin.readline

n,m = map(int,input().split())

s = []
for _ in range(n):
  s.append(input())

w = []
for _ in range(m):
  w.append(input())

count = 0
for i in w:
  if i in s:
    count += 1

print(count)