n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

left = []
right = []

#음수, 양수 구분
for i in data:
    if i < 0:
        left.append(i)
    else:
        right.append(i)

distance = []

#음수에서 들릴 책 꽂이 위치
for i in range(len(left) // m):
    distance.append(abs(left[i * m]))
#홀수 경수
if (len(left) % m) != 0:
    distance.append(abs(left[len(left) // m * m]))

# 양수에서 들릴 책 꽂이 위치
right.sort(reverse=True)
for i in range(len(right) // m):
    distance.append(right[i * m])
#홀수 경우
if (len(right) % m) != 0:
    distance.append(right[len(right) // m * m])

distance.sort()
#제일 먼 책 꽂이 위치는 마지막에 들림. -> 다시 되돌아 오지 않아도 됨.
result = distance.pop()
result += sum(distance) * 2

print(result)