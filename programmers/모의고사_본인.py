def solution(answers):
    answer = []
    case1 = [1, 2, 3, 4, 5]
    case2 = [2, 1, 2, 3, 2, 4, 2, 5]
    case3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    array = [case1, case2, case3]

    for i in range(len(array)):
        while len(answers) > len(array[i]):
            i += i

    result = []
    for i in array:
        count = 0
        for j in range(len(answers)):
            if i[j] == answers[j]:
                count += 1
        else:
            result.append(count)

    max_value = max(result)

    for i in range(len(result)):
        if result[i] == max_value:
            answer.append(i + 1)
    return answer

# 시간초과 !!!!!!!!!!!