n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        # 왼쪽 위
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]

        # 오른쪽 위 - 오른쪽 위의 index는 항상 자신의 index와 같다.
        if j == i:
            up_right = 0
        else:
            up_right = dp[i-1][j]

        dp[i][j] += max(up_left, up_right)

print(max(dp[n-1]))
print(dp)