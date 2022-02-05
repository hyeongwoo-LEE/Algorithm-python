n = int(input())

data = list(map(int, input().split()))

answer = [0]


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


for i in data:
    if answer[-1] < i:
        answer.append(i)
    else:
        answer[binary_search(answer, i, 0, len(answer) - 1)] = i

print(len(answer) - 1)