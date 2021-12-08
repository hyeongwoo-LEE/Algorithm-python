import sys

input = sys.stdin.readline

n,k = map(int,input().split())

value = []
for _ in range(n):
   value.append(int(input()))

value.sort(reverse=True)

count = 0
for i in value:
  count += (k // i)
  if k%i == 0:
    break
  k = (k % i)

print(count)