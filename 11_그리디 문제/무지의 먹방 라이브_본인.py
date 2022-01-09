from collections import deque

def solution(food_times, k):
    q = deque()
    for i in range(len(food_times)):
        q.append((food_times[i], i + 1))

    count = 0
    while q:
        remain, num = q.popleft()
        remain -= 1
        if count == k:
            answer = num
            break

        if remain > 0:
            q.append((remain, num))
        count += 1
    else:
        answer = -1
    return answer

print(solution([3,1,2],5))

#https://programmers.co.kr/learn/courses/30/lessons/42891