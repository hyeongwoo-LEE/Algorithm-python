t = int(input())


def bs(target, data):
    start = 0
    end = len(data) - 1
    index = -1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] < target:
            index = mid
            start = mid + 1
        else:
            end = mid - 1
    return index


for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    count = 0
    for i in a:
        if bs(i, b) >= -1:
            count += bs(i, b) + 1
    print(count)
