def solution(answers):
    answer = []
    case1 = [1, 2, 3, 4, 5]
    case2 = [2, 1, 2, 3, 2, 4, 2, 5]
    case3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0] * 3

    for i in range(len(answers)):
        if answers[i] == case1[i % len(case1)]:
            count[0] += 1

        if answers[i] == case2[i % len(case2)]:
            count[1] += 1

        if answers[i] == case3[i % len(case3)]:
            count[2] += 1

    max_value = max(count)

    if count[0] == max_value:
        answer.append(1)

    if count[1] == max_value:
        answer.append(2)

    if count[2] == max_value:
        answer.append(3)

    return answer