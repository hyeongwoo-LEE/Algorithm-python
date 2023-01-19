n = int(input())

data = []

for _ in range(n):
    data.append(input())

answer = list(data[0])

for i in range(1, n):
    for j in range(len(answer)):
        if answer[j] != data[i][j]:
            answer[j] = '?'

print("".join(answer))