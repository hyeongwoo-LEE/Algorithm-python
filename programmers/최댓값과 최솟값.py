def solution(s):
    data = list(map(int, s.split()))

    min_value = min(data)
    max_value = max(data)

    answer = str(min_value)
    answer += (" " + str(max_value))
    return answer