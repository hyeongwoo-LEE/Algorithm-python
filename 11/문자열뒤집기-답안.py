data = input()

count0 = 0 #0으로 바꾸는 경우
count1 = 0 #1로 바꾸는 경우

if data[0] == 0:
    count1 += 1;
else:
    count0 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        #다음 수가 1일 경우
        if data[i+1] == 1:
            count0 += 1

        #다음 수가 0일 경우
        elif data[i+1] == 0:
            count1 += 1

print(min(count0,count1))

