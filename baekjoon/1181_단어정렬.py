import sys

input = sys.stdin.readline

n = int(input())

data_set = set()

for _ in range(n):
    data_set.add(input().strip())

data_list = []
for i in data_set:
    # (단어,길이)
    data_list.append((i, len(i)))

data_list.sort(key=lambda x: (x[1], x[0]))

for i in data_list:
    print(i[0])