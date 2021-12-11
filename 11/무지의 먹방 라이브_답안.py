import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while (q[0][0] - previous) * length <= (k - sum_value):
        time = heapq.heappop(q)[0]
        sum_value += (time - previous) * length
        length -= 1
        previous = time

    result = sorted(q, key=lambda x: x[1])

    return result[(k - sum_value) % length][1]

print(solution([3,1,2],5))

#https://programmers.co.kr/learn/courses/30/lessons/42891