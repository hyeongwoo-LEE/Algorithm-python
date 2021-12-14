n = int(input())

data = []

for _ in range(n):
    data.append(list(input()))

result_ga = 0
result_se = 0
for i in range(n):
    count_ga = 0
    count_se = 0
    for j in range(n):
        if data[i][j] == '.':
            count_ga += 1
        else:
            if count_ga >= 2:
                result_ga += 1
            count_ga = 0

        if data[j][i] == '.':
            count_se += 1
        else:
            if count_se >= 2:
                result_se += 1
            count_se = 0

    if count_ga >= 2:
        result_ga += 1
    if count_se >= 2:
        result_se += 1

print(result_ga, result_se)