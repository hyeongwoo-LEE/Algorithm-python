n,m = map(int,input().split())

no_listen = set()
no_see = set()

for _ in range(n):
  no_listen.add(input())

for _ in range(m):
  no_see.add(input())

answer = sorted(list(no_listen & no_see))

print(len(answer))
for i in answer:
  print(i)