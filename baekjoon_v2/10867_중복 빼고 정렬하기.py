n = int(input())

set_num = set(map(int,input().split()))

list_num = sorted(list(set_num))

for i in list_num:
  print(i, end=' ')