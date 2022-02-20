n = int(input())

def new_num(n):
    if n < 10:
        num_each = [0]
        num_each.append(n)
    else:
        num_each = [n // 10]
        num_each.append(n % 10)

    sum_num = sum(num_each)
    return int(str(num_each[1]) + str(sum_num % 10))


count = 0
start_num = n
while True:
    i = new_num(start_num)
    count += 1
    if n == i:
        break
    else:
        start_num = i

print(count)

