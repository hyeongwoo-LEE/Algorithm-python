n, m = map(int, input().split())

total_list = list(map(int, input().split()))

negative_list = []
positive_list = []

for i in total_list:
    if i < 0:
        negative_list.append(-i)
    else:
        positive_list.append(i)

negative_list.sort()
positive_list.sort()


def remove(list, m):
    for _ in range(m):
        if len(list) < 1:
            break
        list.pop()


def count_move(list):
    move_cnt = 0

    if len(list) < 1:
        return move_cnt

    while list:
        move_cnt += list[-1] * 2
        remove(list, m)

        if len(list) < 1:
            return move_cnt


# 제일 큰 수가 어느 리스트 있는 지 체크
max_negative = negative_list[-1] if len(negative_list) > 0 else 0
max_positive = positive_list[-1] if len(positive_list) > 0 else 0

if max_negative <= max_positive:
    print(count_move(negative_list) +
          count_move(positive_list) - max_positive)
else:
    print(count_move(positive_list) +
          count_move(negative_list) - max_negative)