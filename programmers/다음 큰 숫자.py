def solution(n):
    answer = 0
    input_count = str(bin(n)).count("1")
    while True:
        n += 1
        find_count = str(bin(n)).count("1")

        if input_count == find_count:
            answer = n
            break
    return answer