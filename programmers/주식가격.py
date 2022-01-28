from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []
    while q:
        price = q.popleft()
        sec = 0
        for i in q:
            sec += 1
            if price > i:
                break
        answer.append(sec)

    return answer