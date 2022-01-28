def solution(phone_book):
    answer = True
    i = 0
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1::]):
        if p2.startswith(p1):
            answer = False
            break
    return answer