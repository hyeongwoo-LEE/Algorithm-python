def count(button):
    global total
    if button > total:
        return 0

    i = 1
    while True:
        if (button * i) > total:
            total -= (button * (i - 1))
            return i - 1
        i += 1

total = int(input())

a = 300
b = 60
c = 10

if (total % 10) == 0:
    print(count(a), end=' ')
    print(count(b), end=' ')
    print(count(c), end=' ')
else:
    print(-1)


