t = int(input())

for _ in range(t):
    w = {}
    n = int(input())
    for _ in range(n):
        name, type = input().split()
        if type in w:
            w[type] += 1
        else:
            w[type] = 1

    case = 1
    for type in w.keys():
        case *= (w[type] + 1)
    # 아예 안 입는 경우 제외
    print(case - 1)