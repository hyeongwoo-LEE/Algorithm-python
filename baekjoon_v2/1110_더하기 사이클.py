def get_next(num):
    str_num = ''

    if num < 10:
        str_num = '0' + str(num)
    else:
        str_num = str(num)

    new_num = int(str_num[0]) + int(str_num[1])

    if new_num < 10:
        return int(str_num[1] + str(new_num))
    else:
        str_new_num = str(new_num)
        return int(str_num[1] + str_new_num[1])


first_num = int(input())
copy_num = first_num
cnt = 0

while True:
    next_num = get_next(copy_num)
    cnt += 1

    if first_num == next_num:
        break

    copy_num = next_num

print(cnt)

